FROM python:3.11

COPY requirements.txt .pre-commit-config.yaml ./
COPY app/source ./source
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 source/manage.py makemigrations
RUN python3 source/manage.py migrate

COPY . .

EXPOSE 8000

CMD ["python3", "source/manage.py", "runserver"]
