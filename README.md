# 🔐 MVP_SecurePlay

Plataforma gamificada para **treinamento em segurança da informação**, voltada a colaboradores corporativos.  
Os usuários avançam através de **níveis Iniciante, Intermediário e Especialista**, respondendo quizzes para ganhar **pontos e badges**.  

O projeto também inclui **análises de segurança automatizadas**, usando OWASP Dependency-Check e Semgrep, para ensinar boas práticas de desenvolvimento seguro.

---

## 🚀 Funcionalidades (MVP)

- **Autenticação de usuários** com JWT via Djoser  
- **Quizzes gamificados** para 3 níveis de dificuldade  
- **Sistema de pontuação e badges**  
- **Interface web responsiva** com Vue.js e Vite  
- **API RESTful** para frontend consumir dados de quizzes e progresso  
- **Banco de dados PostgreSQL** containerizado  
- **Execução simplificada com Docker Compose**  

---

## 🛠 Tecnologias e Ferramentas

| Camada         | Tecnologias/Versões                     |
|----------------|----------------------------------------|
| Backend        | Python 3.11, Django, Django REST, Djoser |
| Frontend       | Vue.js 3, Vite                          |
| Banco de Dados | PostgreSQL                               |
| DevOps         | Docker, Docker Compose                   |
| Segurança      | OWASP Dependency-Check, Semgrep         |

---

## 📂 Estrutura do Projeto


---

## 🐳 Rodando Localmente

### Com Docker

```bash
git clone https://github.com/ViviAkhemi/SecurePlayMVP.git
cd SecurePlayMVP
docker compose up --build -d

Backend: http://localhost:8000
Frontend: http://localhost:5173

Sem Docker (manual)
# Backend
cd backend
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev

⚙️ API Endpoints (Resumo Educativo)

| Endpoint         | Método | Descrição                           | Exemplo de Requisição                       |
| ---------------- | ------ | ----------------------------------- | ------------------------------------------- |
| `/api/token/`    | POST   | Login com username e senha          | `{ "username": "user", "password": "123" }` |
| `/api/lessons/`  | GET    | Lista quizzes disponíveis por nível | `{ "level": 0 }`                            |
| `/api/progress/` | GET    | Consulta progresso do usuário       | —                                           |
| `/api/progress/` | POST   | Atualiza pontos e badges            | `{ "points": 10, "badge": "🥉 Iniciante" }` |
