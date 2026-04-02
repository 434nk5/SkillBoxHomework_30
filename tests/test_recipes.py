import unittest
from pathlib import Path

from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.database import Base, get_session
from app.main import app
from app.models import Recipe

TEST_DB_FILE = Path("test_recipes.db")
TEST_DATABASE_URL = f"sqlite+aiosqlite:///./{TEST_DB_FILE.name}"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = async_sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def override_get_session():
    async with TestSessionLocal() as session:
        yield session


class TestRecipesAPI(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self._remove_test_db_files()

        app.dependency_overrides[get_session] = override_get_session

        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        self.client = AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        )

    async def asyncTearDown(self):
        await self.client.aclose()
        app.dependency_overrides.clear()

        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

        await test_engine.dispose()
        self._remove_test_db_files()

    @staticmethod
    def _remove_test_db_files():
        for file_path in (
            TEST_DB_FILE,
            Path(f"{TEST_DB_FILE}-shm"),
            Path(f"{TEST_DB_FILE}-wal"),
        ):
            if file_path.exists():
                file_path.unlink()

    async def seed_recipes(self):
        async with TestSessionLocal() as session:
            session.add_all(
                [
                    Recipe(
                        title="Салат",
                        cooking_time=15,
                        ingredients=["Огурец", "Помидор"],
                        description="Нарезать и смешать.",
                        views=5,
                    ),
                    Recipe(
                        title="Омлет",
                        cooking_time=10,
                        ingredients=["Яйца", "Молоко"],
                        description="Смешать и обжарить.",
                        views=5,
                    ),
                    Recipe(
                        title="Суп",
                        cooking_time=40,
                        ingredients=["Вода", "Картофель"],
                        description="Сварить.",
                        views=2,
                    ),
                ]
            )
            await session.commit()

    async def test_create_recipe(self):
        payload = {
            "title": "Блины",
            "cooking_time": 20,
            "ingredients": ["Мука", "Молоко", "Яйца"],
            "description": "Смешать ингредиенты и обжарить.",
        }

        response = await self.client.post("/recipes", json=payload)

        self.assertEqual(response.status_code, 201)
        data = response.json()

        self.assertEqual(data["title"], payload["title"])
        self.assertEqual(data["cooking_time"], payload["cooking_time"])
        self.assertEqual(data["ingredients"], payload["ingredients"])
        self.assertEqual(data["description"], payload["description"])
        self.assertEqual(data["views"], 0)
        self.assertIn("id", data)

    async def test_get_recipes_returns_sorted_list(self):
        await self.seed_recipes()

        response = await self.client.get("/recipes")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(len(data), 3)

        self.assertEqual(data[0]["title"], "Омлет")
        self.assertEqual(data[0]["views"], 5)
        self.assertEqual(data[0]["cooking_time"], 10)

        self.assertEqual(data[1]["title"], "Салат")
        self.assertEqual(data[1]["views"], 5)
        self.assertEqual(data[1]["cooking_time"], 15)

        self.assertEqual(data[2]["title"], "Суп")
        self.assertEqual(data[2]["views"], 2)
        self.assertEqual(data[2]["cooking_time"], 40)

    async def test_get_recipe_increments_views(self):
        create_response = await self.client.post(
            "/recipes",
            json={
                "title": "Паста",
                "cooking_time": 25,
                "ingredients": ["Паста", "Сыр"],
                "description": "Отварить и смешать.",
            },
        )
        recipe_id = create_response.json()["id"]

        detail_response = await self.client.get(f"/recipes/{recipe_id}")
        self.assertEqual(detail_response.status_code, 200)

        list_response = await self.client.get("/recipes")
        self.assertEqual(list_response.status_code, 200)

        recipes = list_response.json()
        self.assertEqual(recipes[0]["id"], recipe_id)
        self.assertEqual(recipes[0]["views"], 1)


if __name__ == "__main__":
    unittest.main()
