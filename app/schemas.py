from pydantic import BaseModel, ConfigDict, Field


class RecipeCreate(BaseModel):
    title: str = Field(..., description="Название рецепта", examples=["Омлет"])
    cooking_time: int = Field(
        ...,
        description="Время приготовления в минутах",
        examples=[10],
    )
    ingredients: list[str] = Field(
        ...,
        description="Список ингредиентов",
        examples=[["Яйца", "Молоко", "Соль"]],
    )
    description: str = Field(
        ...,
        description="Текстовое описание рецепта",
        examples=["Смешать ингредиенты и обжарить на сковороде."],
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Омлет",
                "cooking_time": 10,
                "ingredients": ["Яйца", "Молоко", "Соль"],
                "description": "Смешать ингредиенты и обжарить на сковороде.",
            }
        }
    )


class RecipeListItem(BaseModel):
    id: int = Field(..., description="ID рецепта")
    title: str = Field(..., description="Название рецепта")
    views: int = Field(..., description="Количество просмотров")
    cooking_time: int = Field(
        ...,
        description="Время приготовления в минутах",
    )

    model_config = ConfigDict(from_attributes=True)


class RecipeDetail(BaseModel):
    id: int = Field(..., description="ID рецепта")
    title: str = Field(..., description="Название рецепта")
    cooking_time: int = Field(
        ...,
        description="Время приготовления в минутах",
    )
    ingredients: list[str] = Field(..., description="Список ингредиентов")
    description: str = Field(..., description="Текстовое описание рецепта")

    model_config = ConfigDict(from_attributes=True)


class RecipeCreated(BaseModel):
    id: int = Field(..., description="ID созданного рецепта")
    title: str = Field(..., description="Название рецепта")
    cooking_time: int = Field(
        ...,
        description="Время приготовления в минутах",
    )
    ingredients: list[str] = Field(..., description="Список ингредиентов")
    description: str = Field(..., description="Текстовое описание рецепта")
    views: int = Field(..., description="Количество просмотров")

    model_config = ConfigDict(from_attributes=True)
