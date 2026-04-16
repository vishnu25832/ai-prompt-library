FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install django psycopg2-binary redis django-cors-headers

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]