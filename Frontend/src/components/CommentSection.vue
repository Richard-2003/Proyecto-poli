<script setup>
import { ref } from 'vue'

const props = defineProps({
  comments: {
    type: Array,
    required: true,
  },
  postId: {
    type: [String, Number],
    required: true,
  },
})

const newComment = ref('')
const emit = defineEmits(['add-comment'])

const handleSubmit = () => {
  if (newComment.value.trim()) {
    emit('add-comment', {
      postId: props.postId,
      content: newComment.value,
      author: 'Usuario Actual', // En un caso real, esto vendría del sistema de autenticación
      date: new Date().toISOString(),
    })
    newComment.value = ''
  }
}
</script>

<template>
  <section class="comments-section">
    <h3>Comentarios ({{ comments.length }})</h3>

    <!-- Formulario para nuevo comentario -->
    <div class="comment-form">
      <textarea v-model="newComment" placeholder="Escribe tu comentario..." rows="3"></textarea>
      <button @click="handleSubmit" :disabled="!newComment.trim()">Publicar comentario</button>
    </div>

    <!-- Lista de comentarios -->
    <div class="comments-list">
      <article v-for="comment in comments" :key="comment.id" class="comment">
        <div class="comment-header">
          <div class="comment-author">
            <img
              :src="comment.avatar || 'https://ui-avatars.com/api/?name=' + comment.author"
              :alt="comment.author"
            />
            <div class="author-info">
              <strong>{{ comment.author }}</strong>
              <time>{{ new Date(comment.date).toLocaleDateString() }}</time>
            </div>
          </div>
        </div>
        <p class="comment-content">{{ comment.content }}</p>
        <div class="comment-actions">
          <button class="action-btn">
            <i class="far fa-heart"></i>
            <span>Me gusta</span>
          </button>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.comments-section {
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid #eee;
}

.comments-section h3 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.comment-form {
  margin-bottom: 2rem;
}

.comment-form textarea {
  width: 100%;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  resize: vertical;
  font-family: inherit;
  margin-bottom: 1rem;
  transition: border-color 0.3s ease;
}

.comment-form textarea:focus {
  outline: none;
  border-color: #ff7a5a;
}

.comment-form button {
  background-color: #ff7a5a;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.comment-form button:hover {
  background-color: #ff6241;
}

.comment-form button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.comment {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem;
}

.comment-header {
  margin-bottom: 1rem;
}

.comment-author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.comment-author img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-info time {
  font-size: 0.85rem;
  color: #666;
}

.comment-content {
  line-height: 1.6;
  color: #444;
  margin-bottom: 1rem;
}

.comment-actions {
  display: flex;
  gap: 1rem;
}

.action-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.9rem;
  padding: 0.5rem;
  transition: color 0.3s ease;
}

.action-btn:hover {
  color: #ff7a5a;
}

@media (max-width: 768px) {
  .comment {
    padding: 1rem;
  }

  .comment-author {
    gap: 0.5rem;
  }

  .comment-author img {
    width: 32px;
    height: 32px;
  }
}
</style>
