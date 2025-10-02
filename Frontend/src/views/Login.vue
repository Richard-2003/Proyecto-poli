<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

const formData = ref({
  email: '',
  password: '',
  remember: false,
})

const errors = ref({
  email: '',
  password: '',
})

const validateForm = () => {
  let isValid = true
  errors.value = { email: '', password: '' }

  if (!formData.value.email.trim()) {
    errors.value.email = 'Email is required'
    isValid = false
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.email)) {
    errors.value.email = 'Please enter a valid email'
    isValid = false
  }

  if (!formData.value.password) {
    errors.value.password = 'Password is required'
    isValid = false
  }

  return isValid
}

const handleLogin = async () => {
  if (validateForm()) {
    try {
      // Lógica de login
      console.log('Login submitted:', formData.value)
      router.push('/') // redirigir al home tras login
    } catch (error) {
      console.error('Login error:', error)
    }
  }
}

const goToRegister = () => {
  router.push('/register')
}
</script>

<template>
  <Header />
  <main class="login">
    <div class="login-container">
      <h1>Welcome back</h1>
      <p class="subtitle">Log in to continue reading and save your favorite pet posts.</p>

      <form @submit.prevent="handleLogin" class="login-form">
        <!-- Email -->
        <div class="form-group">
          <label for="email">Email Address</label>
          <input
            type="email"
            id="email"
            v-model="formData.email"
            :class="{ 'error-input': errors.email }"
          />
          <span class="error-message" v-if="errors.email">{{ errors.email }}</span>
        </div>

        <!-- Password -->
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="formData.password"
            :class="{ 'error-input': errors.password }"
          />
          <span class="error-message" v-if="errors.password">{{ errors.password }}</span>
        </div>

        <!-- Remember me -->
        <div class="form-group checkbox-group">
          <label>
            <input type="checkbox" v-model="formData.remember" />
            Remember me
          </label>
          <a href="#" class="link">Forgot password?</a>
        </div>

        <!-- Submit -->
        <button type="submit" class="submit-btn">Log In</button>


       <!-- <div class="extra-buttons">
          <button type="button" class="btn-secondary">📧 Email Magic Link</button>
          <button type="button" class="btn-secondary">🐙 GitHub</button>
        </div>  -->

        <!-- Register Link -->
        <p class="register-link">
          New to PetLife?
          <a @click="goToRegister" class="link">Create an account</a>
        </p>
      </form>
    </div>
  </main>
  <Footer />
</template>


<style scoped>
.login {
  min-height: calc(100vh - 140px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background-color: #f8f9fa;
}

.login-container {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 450px;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 0.5rem;
  font-size: 2rem;
}

.subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 2rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: 500;
  color: #444;
}

input[type='email'],
input[type='password'] {
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

input:focus {
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

/* Remember me + Forgot password */
.checkbox-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.95rem;
  color: #444;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.checkbox-group input[type='checkbox'] {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.submit-btn {
  background-color: #ff7a5a;
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 0.5rem;
}

.submit-btn:hover {
  background-color: #ff6241;
}

/*.extra-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 1.5rem;
} */

.btn-secondary {
  background-color: #f1f3f5;
  border: none;
  padding: 0.9rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-secondary:hover {
  background-color: #e2e6ea;
}

.register-link {
  text-align: center;
  margin-top: 1.5rem;
  color: #666;
}

.link {
  color: #ff7a5a;
  text-decoration: none;
  cursor: pointer;
  transition: color 0.3s ease;
}

.link:hover {
  color: #ff6241;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .login {
    padding: 1rem;
  }

  .login-container {
    padding: 1.5rem;
  }

  h1 {
    font-size: 1.75rem;
  }
}
</style>

