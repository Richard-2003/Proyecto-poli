<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import { ref } from 'vue'

//Aquí se haría una conexión con el backend para traer la información del usuario
//Se organizaría mejor luego con manejo de errores
const user = ref({
  name: 'Hola :D',
  email: 'hola@example.com',
  avatar: '', //En realidad no sé si se tiene pensado guardar imagenes de usuario
})

const preferences = ref({
  emailNotifications: true,
  publicProfile: false,
})

//Simulación de actividad reciente del usuario
const recentActivity = ref([
  { id: 1, title: 'How to take care of puppies', date: '2025-09-20' },
  { id: 2, title: 'Top 5 foods for cats', date: '2025-09-18' },
])
</script>

<template>
  <Header />
  <main class="profile">
    <div class="profile-container">
      <!-- Lado Izquierdo: Avatar + acciones -->
      <aside class="profile-sidebar">
        <div class="avatar-wrapper">
          <div v-if="user.avatar" class="avatar">
            <img :src="user.avatar" alt="User avatar" />
          </div>
          <div v-else class="avatar placeholder">
            <span>🐾</span>
          </div>
        </div>

        <h2 class="user-name">{{ user.name }}</h2>
        <p class="user-email">{{ user.email }}</p>

        <button class="edit-btn">Editar perfil</button>
        <a href="/createPost">
        <button class="edit-btn">Crear Post</button>
        </a>
      </aside>

      <!-- Lado Derecho: Info -->
      <section class="profile-content">
        <div class="info-card">
          <h3>Sobre mí</h3>
          <!-- <p>{{ user.bio }}</p> -->
        </div>

        <!-- Actividad reciente -->
        <div class="info-card">
          <h3>Recent Activity</h3>
          <ul>
            <li v-for="activity in recentActivity" :key="activity.id">
              <strong>{{ activity.title }}</strong>
              <span class="date">{{ activity.date }}</span>
            </li>
          </ul>
        </div>

        <!-- Cosas de seguirdad -->
        <div class="info-card">
          <h3>Security</h3>
          <button class="btn-secondary">Change Password</button>
          <button class="btn-secondary">Log Out</button>
        </div>
      </section>
    </div> 
  </main>
  <Footer />
</template>


<style scoped>
/* --- Layout base --- */
.profile {
  min-height: calc(100vh - 140px); 
  background-color: #f8f9fa;
  padding: 2rem;
  display: flex;
  justify-content: center;
}

.profile-container {
  display: grid;
  grid-template-columns: 1fr; /* mobile: 1 columna */
  gap: 2rem;
  width: 100%;
  max-width: 1000px;
}

/* --- Sidebar (izquierda) --- */
.profile-sidebar {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.avatar-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid #ff7a5a;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar.placeholder {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 3px dashed #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  color: #999;
}

.user-name {
  margin-top: 0.5rem;
  font-size: 1.5rem;
  color: #333;
}

.user-email {
  color: #666;
  margin-bottom: 1rem;
}

.edit-btn {
  background-color: #ff7a5a;
  color: white;
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.edit-btn:hover {
  background-color: #ff6241;
}

.btn-secondary {
  background-color: #f1f3f5;
  border: none;
  padding: 0.8rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  width: 100%;
  margin-top: 0.5rem;
}

/* --- Content (derecha) --- */
.profile-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.info-card h3 {
  margin-bottom: 0.5rem;
  color: #333;
}

/* --- Responsive --- */
@media (min-width: 768px) {
  .profile-container {
    grid-template-columns: 1fr 2fr; /* en pantallas grandes: sidebar + contenido */
  }

  .profile-sidebar {
    text-align: left;
    align-self: start;
  }

  .avatar-wrapper {
    justify-content: flex-start;
  }
}
</style>