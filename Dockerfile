FROM python:3.11

COPY requirements.txt .pre-commit-config.yaml ./
COPY django-app/pyDB ./django-app/pyDB
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 django-app/pyDB/manage.py makemigrations
RUN python3 django-app/pyDB/manage.py migrate

COPY . .

CMD ["python3", "source/manage.py", "runserver"]
