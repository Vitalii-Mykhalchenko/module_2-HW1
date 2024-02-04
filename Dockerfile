# Використовуємо офіційний образ Python з версією, яку хочемо встановити
FROM python:3.11.6

# Вказуємо робочий каталог
WORKDIR /app

# Встановлюємо необхідні залежності
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копіюємо файли додатка в контейнер
COPY  src/main.py /app/src/
COPY  src/notes.py /app/src/
COPY  src/classes.py /app/src/
COPY  src/sorter.py /app/src/
COPY  src/user_interface.py /app/src/


# Запускаємо додаток
CMD ["python", "src/main.py"]