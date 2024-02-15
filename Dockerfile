FROM python:3.11

WORKDIR /app

COPY requirements.txt .pre-commit-config.yaml ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000