<template>
  <div class="quiz-container">
    <!-- TELA LOGIN -->
    <div v-if="screen === 'login'">
      <h2>Login</h2>
      <input v-model="username" placeholder="Usuário" />
      <input v-model="password" type="password" placeholder="Senha" />
      <button @click="login">Entrar</button>
      <p v-if="loginError" class="error">Usuário ou senha inválidos.</p>
    </div>

    <!-- TELA MENU -->
    <div v-else-if="screen === 'menu'">
      <h2>Bem-vindo, {{ username || 'Usuário'  }}!</h2>
      <p>Escolha seu nível:</p>
      <button @click="startLevel(0)">🥉 Iniciante</button>
      <button @click="startLevel(1)">🥈 Intermediário</button>
      <button @click="startLevel(2)">🥇 Especialista</button>
      <hr />
      <p><strong>Medalhas conquistadas:</strong> {{ badges.join(' | ') || 'Nenhuma' }}</p>
      <p><strong>Pontos acumulados:</strong> ⭐ {{ points }}</p>
    </div>

    <!-- TELA QUIZ -->
    <div v-else-if="screen === 'quiz'">
      <div class="status-bar">
        <p>Pontos: ⭐ {{ points }}</p>
        <p>Medalhas: {{ badges.join(' | ') || 'Nenhuma' }}</p>
      </div>

      <h2>{{ currentQuestion.question }}</h2>

      <ul>
        <li
          v-for="(option, index) in currentQuestion.options"
          :key="index"
          :class="getOptionClass(index)"
          @click="selectOption(index)"
        >
          {{ option }}
          <span v-if="selected === index">
            <template v-if="isCorrect(index)">✅</template>
            <template v-else>❌</template>
          </span>
        </li>
      </ul>

      <div v-if="selected !== null" class="feedback">
        <p v-if="isCorrect(selected)">
          Muito bem!!! Você ganhou 10 pontos. <br />
          Vamos para o próximo desafio 🎉
        </p>
        <p v-else>Boa tentativa, continue praticando!</p>
        <button @click="nextQuestion">Próximo desafio</button>
      </div>
    </div>

    <!-- TELA FINAL DE CADA NÍVEL -->
    <div v-else-if="screen === 'end'">
      <h2>Parabéns! Você concluiu o nível {{ badgeNames[currentLevel] }}</h2>
      <p>Pontos acumulados: ⭐ {{ points }}</p>
      <p>Medalhas conquistadas: {{ badges.join(' | ') }}</p>
      <button @click="restart">Voltar ao menu</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const screen = ref('login')  // telas: 'login', 'menu', 'quiz', 'end'

const username = ref('')
const password = ref('')
const loginError = ref(false)

const levels = [
  [ // Iniciante
    {
      question: "Qual é a senha mais forte?",
      options: ["Ana2024", "123456", "@na_Segura!2025"],
      answer: 2,
    },
    {
      question: "O que acontece ao escolher uma senha fraca?",
      options: ["nada muda", "você ganha pontos", "sua conta fica vulnerável"],
      answer: 2,
    },
  ],
  [ // Intermediário
    {
      question: "Qual das opções representa melhor o que é um malware?",
      options: [
        "Um programa de segurança instalado pelo próprio usuário.",
        "Um software malicioso criado para causar danos, roubar dados ou espionar.",
        "Um sistema legítimo que atualiza automaticamente o antivírus.",
      ],
      answer: 1,
    },
    {
      question:
        "Se você está desenvolvendo um sistema de cadastro de usuários, qual medida aumenta a segurança contra ataques de phishing?",
      options: [
        "Exigir autenticação multifator no login",
        "Permitir login com senha simples para melhorar a experiência do usuário.",
        "Enviar links de redefinição de senha sem expiração.",
      ],
      answer: 0,
    },
  ],
  [ // Especialista
    {
      question:
        "Um tipo de malware projetado para registrar tudo o que o usuário digita no teclado é chamado de:",
      options: ["Ramsomware", "Keylogger", "Worm"],
      answer: 1,
    },
    {
      question:
        "No desenvolvimento de uma API que exige autenticação, qual prática é mais segura contra abusos relacionados a phishing?",
      options: [
        "Usar tokens de acesso de curta duração com renovação segura.",
        "Utilizar login apenas com senha para simplificar a experiência.",
        "Armazenar tokens permanentemente no navegador do usuário.",
      ],
      answer: 0,
    },
  ],
]

const badgeNames = ['🥉 Iniciante', '🥈 Intermediário', '🥇 Especialista']

const currentLevel = ref(null)
const currentIndex = ref(0)
const selected = ref(null)
const correctStreak = ref(0)

const points = ref(0)
const badges = ref([])

const currentQuestion = computed(() => {
  if (currentLevel.value === null) return null
  return levels[currentLevel.value][currentIndex.value]
})

async function login() {
  loginError.value = false
  try {
    const response = await fetch('http://localhost:8000/api/token/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })

    if (!response.ok) {
      loginError.value = true
      return
    }

    const data = await response.json()

    // Salva os tokens no localStorage
    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    screen.value = 'menu'
    loginError.value = false
  } catch (error) {
    console.error('Erro no login:', error)
    loginError.value = true
  }
}

function startLevel(level) {
  currentLevel.value = level
  currentIndex.value = 0
  selected.value = null
  correctStreak.value = 0
  screen.value = 'quiz'
}

function selectOption(index) {
  if (selected.value === null) {
    selected.value = index
    if (isCorrect(index)) {
      points.value += 10
      correctStreak.value++
    } else {
      correctStreak.value = 0
    }
  }
}

function isCorrect(index) {
  return index === currentQuestion.value.answer
}

function getOptionClass(index) {
  if (selected.value === null) return ''
  if (index === currentQuestion.value.answer) return 'correct'
  if (index === selected.value && !isCorrect(selected.value)) return 'wrong'
  return ''
}

function nextQuestion() {
  if (currentIndex.value < levels[currentLevel.value].length - 1) {
    currentIndex.value++
    selected.value = null
  } else {
    // Se acertou todas, ganha medalha e vai para tela final do nível
    if (correctStreak.value === levels[currentLevel.value].length) {
      awardBadge(currentLevel.value)
      screen.value = 'end'
    } else {
      // Errou, reinicia o mesmo nível para tentar de novo
      alert('Você precisa acertar todas para finalizar este nível.')
      currentIndex.value = 0
      selected.value = null
      correctStreak.value = 0
    }
  }
}

function awardBadge(level) {
  const badge = badgeNames[level]
  if (!badges.value.includes(badge)) {
    badges.value.push(badge)
    alert(`🏅 Você ganhou a medalha: ${badge}!`)
  }
}

function restart() {
  screen.value = 'menu'
  currentLevel.value = null
  currentIndex.value = 0
  selected.value = null
  correctStreak.value = 0
}
</script>


<style scoped>
.quiz-container {
  max-width: 500px;
  margin: 2rem auto;
  font-family: Arial, sans-serif;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
}

.status-bar {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding: 0.5rem;
  background: #f8f9fa;
  border-radius: 6px;
  font-weight: bold;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border: 1px solid #ddd;
  margin-bottom: 8px;
  cursor: pointer;
  border-radius: 4px;
  user-select: none;
  transition: background-color 0.3s ease;
}

li.correct {
  background-color: #d4edda;
  border-color: #28a745;
  color: #155724;
}

li.wrong {
  background-color: #f8d7da;
  border-color: #dc3545;
  color: #721c24;
}

.feedback {
  margin-top: 20px;
}

button {
  cursor: pointer;
  padding: 8px 16px;
  margin-top: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  border-radius: 4px;
  font-size: 1rem;
}

button:hover {
  background-color: #0056b3;
}

input {
  display: block;
  margin-bottom: 10px;
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

.error {
  color: red;
  margin-top: 5px;
}
</style>
