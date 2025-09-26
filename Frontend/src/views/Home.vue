<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import PostCard from '@/components/PostCard.vue'

// Simulación de datos de posts (luego esto vendrá de una API o store)
const posts = [
  {
    id: 1,
    title: 'Tips para el cuidado de tu perro en verano',
    image: 'https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?ixlib=rb-4.0.3',
    excerpt: 'Descubre cómo mantener a tu mascota fresca y saludable durante los días calurosos...',
    author: 'María García',
    date: '2025-09-20',
    comments: 15,
    likes: 45,
  },
  {
    id: 2,
    title: 'Alimentación saludable para gatos',
    image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3',
    excerpt: 'Guía completa sobre la nutrición felina y las mejores opciones de alimentos...',
    author: 'Carlos Ruiz',
    date: '2025-09-19',
    comments: 23,
    likes: 67,
  },
  {
    id: 3,
    title: 'Ejercicios para mantener activo a tu conejo',
    image: 'https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?ixlib=rb-4.0.3',
    excerpt: 'Aprende diferentes actividades para mantener a tu conejo en forma y feliz...',
    author: 'Ana Martínez',
    date: '2025-09-18',
    comments: 8,
    likes: 34,
  },
]
</script>

<template>
  <Header />
  <!-- Contenido principal de la página -->
  <main>
    <section class="latest-posts">
      <h2>Latest Posts</h2>
      <div class="posts-grid">
        <PostCard v-for="post in posts" :key="post.id" :post="post" />
      </div>
    </section>
  </main>
  <Footer />
</template>

<style scoped>
main {
  max-width: 100%;
  margin: 0 auto;
  padding: 2rem;
}

.latest-posts h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

/* Responsive design */
@media (max-width: 768px) {
  .posts-grid {
    grid-template-columns: 1fr;
  }

  main {
    padding: 1rem;
  }
}
</style>
