# Перетворення Хафа

## Запуск програми

Запустити run.bat.

Або виконати наступні команди:

1. Встановлення залежностей:

    pip install --no-index --find-links=app/downloaded -r app/requirements.txt

2. Власне запуск програми:

    python app/app.py

## Інтерфейс

1. Обрати звідки беруться вихідні дані (власні або існуючі).
2. Обрати дані або завантажити їх.

Для додання інших датасетів можливо через створення папок з зображеннями у папці "datasets".

3. Обрати тип перетворення.
4. Натиснути Почати/Start.
5. Зберегти результат, натиснувши Зберегти/Save.
Зображення будуть збереженні у папці result/<поточний час>.
6. Очистити завантаженні дані, натиснувши Очистити/Clear.

