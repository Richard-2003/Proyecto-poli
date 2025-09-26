<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import CommentSection from '@/components/CommentSection.vue'

const route = useRoute()
const router = useRouter()
const postId = route.params.id
const post = ref(null)
const loading = ref(true)
const error = ref(null)
const comments = ref([
  {
    id: 1,
    postId: 1,
    author: 'Laura Pérez',
    content:
      '¡Excelentes consejos! Especialmente lo del asfalto caliente, mucha gente no lo tiene en cuenta.',
    date: '2025-09-21T10:30:00',
    avatar: 'https://ui-avatars.com/api/?name=Laura+Perez',
  },
  {
    id: 2,
    postId: 1,
    author: 'Carlos Rodríguez',
    content: 'Yo siempre llevo un bebedero plegable en los paseos de verano. Es super práctico.',
    date: '2025-09-21T11:15:00',
    avatar: 'https://ui-avatars.com/api/?name=Carlos+Rodriguez',
  },
])

// Simulación de datos (en un caso real, esto vendría de una API)
const posts = {
  1: {
    id: 1,
    title: 'Tips para el cuidado de tu perro en verano',
    image: 'https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?ixlib=rb-4.0.3',
    content: `
      El verano puede ser una época desafiante para nuestros amigos caninos. Aquí te presentamos algunos consejos esenciales:

      1. Hidratación constante
      - Mantén siempre agua fresca disponible
      - Considera llevar un bebedero portátil en los paseos
      - Cambia el agua varias veces al día

      2. Protección del calor
      - Evita paseos en las horas más calurosas
      - Proporciona áreas con sombra
      - Nunca dejes a tu perro en el carro

      3. Cuidados especiales
      - Revisa el asfalto antes de los paseos
      - Considera un corte de pelo apropiado
      - Usa protector solar en zonas sensibles
    `,
    author: 'María García',
    date: '2025-09-20',
    comments: 15,
    likes: 45,
    readTime: '5 minutos',
    tags: ['Perros', 'Cuidados', 'Verano', 'Salud'],
  },
  // Otros posts...
}

const loadPost = () => {
  loading.value = true
  error.value = null

  // Simulando una llamada a API
  setTimeout(() => {
    const foundPost = posts[postId]
    if (foundPost) {
      post.value = foundPost
      loading.value = false
    } else {
      error.value = 'Post no encontrado'
      loading.value = false
    }
  }, 500)
}

const handleAddComment = (newComment) => {
  const comment = {
    id: comments.value.length + 1,
    ...newComment,
  }
  comments.value.unshift(comment) // Añade el comentario al principio de la lista
}
const goBack = () => {
  router.push('/')
}

onMounted(() => {
  loadPost()
})
</script>

<template>
  <Header />
  <main class="post-detail">
    <div v-if="loading" class="loading">Cargando...</div>

    <div v-else-if="error" class="error">
      {{ error }}
      <button @click="goBack" class="back-button">Volver al inicio</button>
    </div>

    <div v-else-if="post" class="container">
      <button @click="goBack" class="back-button"><i class="fas fa-arrow-left"></i> Volver</button>

      <div class="post-header">
        <h1>{{ post.title }}</h1>
        <div class="post-meta">
          <div class="author-info">
            <i class="fas fa-user"></i>
            <span>{{ post.author }}</span>
          </div>
          <div class="post-details">
            <span class="date">
              <i class="far fa-calendar"></i>
              {{ new Date(post.date).toLocaleDateString() }}
            </span>
            <span class="read-time">
              <i class="far fa-clock"></i>
              {{ post.readTime }}
            </span>
          </div>
        </div>
      </div>

      <div class="post-image">
        <img :src="post.image" :alt="post.title" />
      </div>

      <div class="post-content" v-html="post.content"></div>

      <div class="post-footer">
        <div class="tags">
          <span v-for="tag in post.tags" :key="tag" class="tag"> #{{ tag }} </span>
        </div>
        <div class="interactions">
          <button class="like-btn">
            <i class="fas fa-heart"></i>
            <span>{{ post.likes }} Me gusta</span>
          </button>
        </div>
      </div>

      <!-- Sección de comentarios -->
      <CommentSection
        :comments="comments"
        :post-id="Number(postId)"
        @add-comment="handleAddComment"
      />
    </div>
  </main>
  <Footer />
</template>

<style scoped>
.post-detail {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.container {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.loading,
.error {
  text-align: center;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.back-button {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  padding: 0.5rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  transition: color 0.3s ease;
}

.back-button:hover {
  color: #ff7a5a;
}

.post-header {
  margin-bottom: 2rem;
}

.post-header h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #666;
  font-size: 0.9rem;
}

.author-info,
.post-details {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.post-image {
  width: 100%;
  height: 400px;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 2rem;
}

.post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.post-content {
  line-height: 1.8;
  color: #444;
  white-space: pre-wrap;
}

.post-footer {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.tag {
  background: #f0f0f0;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.9rem;
  color: #666;
}

.interactions {
  display: flex;
  gap: 1rem;
}

.like-btn {
  background-color: white;
  border: 2px solid #ff7a5a;
  color: #ff7a5a;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.2rem;
  border-radius: 25px;
  font-weight: 500;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.like-btn:hover {
  background-color: #ff7a5a;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(255, 122, 90, 0.2);
}

.like-btn i {
  font-size: 1.2rem;
}

.error {
  color: #e74c3c;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

i {
  margin-right: 0.3rem;
}

@media (max-width: 768px) {
  .post-detail {
    padding: 1rem;
  }

  .post-header h1 {
    font-size: 2rem;
  }

  .post-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .post-image {
    height: 250px;
  }
}
</style>
