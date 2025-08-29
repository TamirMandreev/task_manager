FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

EXPOSE 8000

CMD python3 manage.py migrate \
    && python3 manage.py runserver 0.0.0.0:8000


