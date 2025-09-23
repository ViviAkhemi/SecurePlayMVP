FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copia só o arquivo requirements para usar cache do Docker quando não mudar
COPY requirements.pip.txt .

RUN pip install --no-cache-dir -r requirements.pip.txt

# Copia o restante do código só depois das dependências instaladas
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
