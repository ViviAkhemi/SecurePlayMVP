# backend/Dockerfile

FROM python:3.11-slim

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza o sistema e instala dependências nativas (se precisar)
# (Use apenas se seus pacotes do requirements precisarem de bibliotecas nativas)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os requirements primeiro (melhora o cache do Docker)
COPY requirements.pip.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.pip.txt

# Copia todo o restante do projeto
COPY . .

# Expõe a porta padrão usada pelo Django
EXPOSE 8000

# Comando padrão para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

