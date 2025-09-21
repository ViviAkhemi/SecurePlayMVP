##### ⚠️ Nota importante

Este repositório tem como objetivo fornecer recursos educacionais.  
Por favor, utilize-o de forma responsável e respeitando as limitações de uso para fins não comerciais.


# 🔐 MVP_SecurePlay

Plataforma gamificada para treinamento em **segurança da informação** voltada a colaboradores corporativos, com foco em níveis **Iniciante**, **Intermediário** e  **Especialista**. Criado com Django (backend) e Vue.js (frontend), usando Docker e PostgreSQL.

---

## 🚀 Funcionalidades (MVP)

- ✅ Login com usuário e senha
- ✅ Desafios para usuários iniciantes, intermediários, especialistas
- ✅ Sistema de pontuação e badges
- ✅ Interface web com Vue.js
- ✅ Backend com API REST em Django
- ✅ Banco de dados PostgreSQL (em container)
- ✅ Docker Compose para fácil execução local


## 🚀 Rodando localmente com Docker

```bash
docker compose up --build -d

Acesse em: http://localhost:5173


## 🛠 Tecnologias Usadas

- **Backend:** Python 3.11, Django, Django REST Framework, Djoser (auth)
- **Frontend:** Vue.js 3, Vite
- **Banco de Dados:** PostgreSQL
- **DevOps:** Docker, Docker Compose
- **Docker

---

### 1. Clone este repositório

```bash
git clone https://github.com/ViviAkhemi/SecurePlayMVP,git
cd SecurePlayMVP

docker-compose up --build

Backend rodando em: http://localhost:8000

Frontend rodando em: http://localhost:5173

SecurePlayMVP/
├── backend/
│   ├── core/           # Projeto Django
│   ├── users/          # Autenticação e perfis
│   ├── lessons/        # Conteúdos gamificados
│   ├── progress/       # Progresso e badges
├── frontend/
│   └── App.vue/   # Projeto Vue.js
├── docker-compose.yml
├── README.md
