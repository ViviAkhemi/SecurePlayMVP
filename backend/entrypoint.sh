#!/bin/bash
set -e

# Espera o banco
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Postgres up"

# Roda as migrações
python manage.py migrate

# Inicia o servidor
exec "$@"
