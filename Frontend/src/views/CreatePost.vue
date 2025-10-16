<script setup>
import { ref } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const postData = ref({
  title: '',
  excerpt: '',
  coverImage: null,
  content: '',
  category: '',
  tags: '',
})

const previewImage = ref(null)
const errors = ref({})

//Subida de la imagen (tampoco estoy segura de cómo se van a guardar las imagenes en la base de datos)
const handleImageUpload = (e) => {
  const file = e.target.files[0]
  if (file && file.type.startsWith('image/')) {
    postData.value.coverImage = file
    previewImage.value = URL.createObjectURL(file)
  } else {
    errors.value.coverImage = 'Please upload a valid image (JPG or PNG)'
  }
}

//Validar formulario básico
const validateForm = () => {
  errors.value = {}
  if (!postData.value.title.trim()) errors.value.title = 'Title is required'
  if (!postData.value.excerpt.trim()) errors.value.excerpt = 'Excerpt is required'
  if (!postData.value.content.trim()) errors.value.content = 'Content is required'
  return Object.keys(errors.value).length === 0
}

//Simular guardar borrador, aunque creo que no vamos a guardar un borrador al final
//así que el botón y esto podrían borrarse
const saveDraft = () => {
  console.log('Borrador guardado:', postData.value)
  alert('Borrador guardado')
}

//Simular publicar post
const publishPost = () => {
  if (validateForm()) {
    console.log('Post publicado:', postData.value)
    alert('Post publicado correctamente')
  } else {
    alert('Por favor complete todos los campos')
  }
}
</script>

<template>
  <Header />
  <main class="create-post">
    <div class="create-container">
      <h1>Create New Post</h1>

      <!--Title-->
      <div class="form-group">
        <label for="title">Post title</label>
        <input
          id="title"
          type="text"
          v-model="postData.title"
          :class="{ 'error-input': errors.title }"
          placeholder="Enter a title..."
        />
        <span v-if="errors.title" class="error-message">{{ errors.title }}</span>
      </div>

      <!--Excerpt-->
      <div class="form-group">
        <label for="excerpt">Short excerpt (140–200 chars)</label>
        <textarea
          id="excerpt"
          rows="2"
          maxlength="200"
          v-model="postData.excerpt"
          :class="{ 'error-input': errors.excerpt }"
          placeholder="Write a short summary..."
        ></textarea>
        <span v-if="errors.excerpt" class="error-message">{{ errors.excerpt }}</span>
      </div>

      <!--Cover Image-->
      <div class="form-group">
        <label for="cover">Cover Image</label>
        <input
          type="file"
          id="cover"
          accept="image/*"
          @change="handleImageUpload"
        />
        <span v-if="errors.coverImage" class="error-message">{{ errors.coverImage }}</span>
        <div v-if="previewImage" class="image-preview">
          <img :src="previewImage" alt="Cover preview" />
        </div>
      </div>

      <!--Post Content-->
      <div class="form-group">
        <label for="content">Write your post content here</label>
        <textarea
          id="content"
          rows="8"
          v-model="postData.content"
          :class="{ 'error-input': errors.content }"
          placeholder="Start writing your post..."
        ></textarea>
        <span v-if="errors.content" class="error-message">{{ errors.content }}</span>
      </div>

      <!--Category-->
      <!--Según yo, debería haber una tabla de categorias y que aquí en lugar de escribir una
      se muestren las categorias existentes y sea un selector -->
      <div class="form-group">
        <label for="category">Category (e.g., Training, Health)</label>
        <input
          id="category"
          type="text"
          v-model="postData.category"
          placeholder="Enter a category..."
        />
      </div>

      <!--Tags-->
      <div class="form-group">
        <label for="tags">Tags (comma separated)</label>
        <input
          id="tags"
          type="text"
          v-model="postData.tags"
          placeholder="e.g., training, health, safety"
        />
      </div>

      <!--Buttons-->
      <div class="btn-group">
        <button class="btn-secondary" @click="saveDraft"> Save Draft</button>
        <button class="btn-primary" @click="publishPost"> Publish</button>
      </div>
    </div>
  </main>
  <Footer />
</template>

<style scoped>
.create-post {
  background-color: #f8f9fa;
  padding: 2rem 1rem;
  display: flex;
  justify-content: center;
}

.create-container {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  color: #333;
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  text-align: left;
}

label {
  font-weight: 500;
  color: #444;
}

input,
textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #ff7a5a;
}

.error-input {
  border-color: #dc3545 !important;
}

.error-message {
  color: #dc3545;
  font-size: 0.875rem;
}

.image-preview {
  margin-top: 0.8rem;
}

.image-preview img {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid #eee;
}

/* Buttons */
.btn-group {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1rem;
}

.btn-primary,
.btn-secondary {
  padding: 0.9rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #ff7a5a;
  color: white;
}

.btn-primary:hover {
  background-color: #ff6241;
}

.btn-secondary {
  background-color: #f1f3f5;
  color: #333;
}

.btn-secondary:hover {
  background-color: #e2e6ea;
}

@media (max-width: 768px) {
  .create-container {
    padding: 1.5rem;
  }

  h1 {
    font-size: 1.5rem;
  }
}
</style>
