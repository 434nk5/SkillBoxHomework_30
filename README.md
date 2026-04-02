# API кулинарной книги

## Что сделано
- `GET /recipes` — получить список рецептов
- `GET /recipes/{recipe_id}` — получить рецепт по ID и увеличить просмотры
- `POST /recipes` — создать новый рецепт
- настроены линтеры: `flake8`, `black`, `isort`, `mypy`
- настроен CI через GitHub Actions

## Установка
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Локальная проверка
```bash
isort . --check-only
black . --check
flake8 .
mypy .
pytest -q
```

## Запуск приложения
```bash
uvicorn app.main:app --reload
```

## Документация
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
