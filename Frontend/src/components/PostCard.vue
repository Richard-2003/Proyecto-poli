<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
  post: {
    type: Object,
    required: true,
  },
})

const navigateToPost = () => {
  router.push(`/post/${props.post.id}`)
}
</script>

<template>
  <article class="post-card" @click="navigateToPost" role="button" tabindex="0">
    <div class="post-image">
      <img :src="post.image" :alt="post.title" />
    </div>
    <div class="post-content">
      <h3>{{ post.title }}</h3>
      <p class="post-excerpt">{{ post.excerpt }}</p>
      <div class="post-meta">
        <div class="author-date">
          <span class="author"> <i class="fas fa-user"></i> {{ post.author }} </span>
          <span class="date">
            <i class="far fa-calendar"></i> {{ new Date(post.date).toLocaleDateString() }}
          </span>
        </div>
        <div class="interactions">
          <span class="comments"> <i class="far fa-comment"></i> {{ post.comments }} </span>
          <span class="likes"> <i class="far fa-heart"></i> {{ post.likes }} </span>
        </div>
      </div>
    </div>
  </article>
</template>

<style scoped>
.post-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
  outline: none;
}

.post-card:focus {
  box-shadow:
    0 0 0 3px #ff7a5a44,
    0 4px 6px rgba(0, 0, 0, 0.1);
}

.post-card:hover {
  transform: translateY(-5px);
}

.post-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.post-card:hover .post-image img {
  transform: scale(1.05);
}

.post-content {
  padding: 1.5rem;
}

.post-content h3 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  color: #333;
}

.post-excerpt {
  color: #666;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: #777;
}

.author-date,
.interactions {
  display: flex;
  gap: 1rem;
}

.post-meta i {
  margin-right: 0.3rem;
}
</style>
