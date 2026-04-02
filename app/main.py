from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import Base, engine, get_session
from .models import Recipe
from .schemas import RecipeCreate, RecipeCreated, RecipeDetail, RecipeListItem


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="API кулинарной книги",
    description=(
        "Сервис для хранения рецептов. "
        "Поддерживает получение списка рецептов, просмотр детальной "
        "информации и создание нового рецепта."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.get(
    "/recipes",
    response_model=list[RecipeListItem],
    summary="Получить список рецептов",
    description=(
        "Возвращает все рецепты. "
        "Сортировка: сначала по количеству просмотров по убыванию, "
        "при равенстве — по времени приготовления по возрастанию."
    ),
    response_description="Список рецептов для таблицы",
)
async def get_recipes(session: SessionDep):
    result = await session.execute(
        select(Recipe).order_by(Recipe.views.desc(), Recipe.cooking_time.asc())
    )
    return result.scalars().all()


@app.get(
    "/recipes/{recipe_id}",
    response_model=RecipeDetail,
    summary="Получить рецепт по ID",
    description=(
        "Возвращает детальную информацию по рецепту. "
        "При каждом открытии детальной страницы количество просмотров "
        "увеличивается на 1."
    ),
    responses={
        404: {
            "description": "Рецепт не найден",
            "content": {
                "application/json": {
                    "example": {"detail": "Рецепт не найден"},
                }
            },
        }
    },
)
async def get_recipe(recipe_id: int, session: SessionDep):
    recipe = await session.get(Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(status_code=404, detail="Рецепт не найден")

    recipe.views += 1
    await session.commit()
    await session.refresh(recipe)

    return recipe


@app.post(
    "/recipes",
    response_model=RecipeCreated,
    status_code=status.HTTP_201_CREATED,
    summary="Создать рецепт",
    description="Создаёт новый рецепт и возвращает созданную запись.",
    response_description="Созданный рецепт",
)
async def create_recipe(data: RecipeCreate, session: SessionDep):
    recipe = Recipe(
        title=data.title,
        cooking_time=data.cooking_time,
        ingredients=data.ingredients,
        description=data.description,
        views=0,
    )

    session.add(recipe)
    await session.commit()
    await session.refresh(recipe)

    return recipe
