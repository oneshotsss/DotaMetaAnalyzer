# DotaMetaAnalyzer

DotaMetaAnalyzer — це pet-проект для аналізу мети Dota 2 на основі статистики героїв та предметів.

## Можливості
- Додавання, перегляд, редагення та видалення героїв і предметів
- Аналітика: топ герої та предмети за winrate
- REST API (FastAPI) з інтерактивною документацією (Swagger UI)
- Зберігання даних у SQLite (dota2.db)

## Швидкий старт
1. Встанови залежності:
   ```bash
   pip install -r requirements.txt
   ```
2. Запусти сервер:
   ```bash
   uvicorn main:app --reload
   ```
3. Відкрий Swagger UI у браузері:
   [http://localhost:8000/docs](http://localhost:8000/docs)

## Docker

Щоб запустити проект у Docker:

1. Побудуй образ:
   ```bash
   docker build -t dota-meta-analyzer .
   ```
2. Запусти контейнер:
   ```bash
   docker run -p 8000:8000 dota-meta-analyzer
   ```
3. Відкрий Swagger UI у браузері:
   [http://localhost:8000/docs](http://localhost:8000/docs)

## Основні ендпоінти
- `/api/v1/heroes` — робота з героями
- `/api/v1/items` — робота з предметами
- `/api/v1/analytics/top-heroes` — топ герої за winrate
- `/api/v1/analytics/top-items` — топ предмети за winrate

## Тестування
```bash
pytest
```

**Автор:** 10am12pm
