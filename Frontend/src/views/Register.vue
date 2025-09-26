<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

const formData = ref({
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  confirmPassword: '',
  agreeTerms: false,
})

const errors = ref({
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  confirmPassword: '',
  agreeTerms: '',
})

const validateForm = () => {
  let isValid = true
  errors.value = {
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: '',
    agreeTerms: '',
  }

  if (!formData.value.firstName.trim()) {
    errors.value.firstName = 'First name is required'
    isValid = false
  }

  if (!formData.value.lastName.trim()) {
    errors.value.lastName = 'Last name is required'
    isValid = false
  }

  if (!formData.value.email.trim()) {
    errors.value.email = 'Email is required'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.email)) {
    errors.value.email = 'Please enter a valid email'
    isValid = false
  }

  if (!formData.value.password) {
    errors.value.password = 'Password is required'
    isValid = false
  } else if (formData.value.password.length < 8) {
    errors.value.password = 'Password must be at least 8 characters'
    isValid = false
  }

  if (!formData.value.confirmPassword) {
    errors.value.confirmPassword = 'Please confirm your password'
    isValid = false
  } else if (formData.value.password !== formData.value.confirmPassword) {
    errors.value.confirmPassword = 'Passwords do not match'
    isValid = false
  }

  if (!formData.value.agreeTerms) {
    errors.value.agreeTerms = 'You must agree to the terms and privacy policy'
    isValid = false
  }

  return isValid
}

const handleSubmit = async () => {
  if (validateForm()) {
    try {
      // Aquí iría la lógica para registrar al usuario
      console.log('Form submitted:', formData.value)
      // Después de un registro exitoso, redirigir al login
      router.push('/login')
    } catch (error) {
      console.error('Registration error:', error)
    }
  }
}

const goToLogin = () => {
  router.push('/login')
}
</script>

<template>
  <Header />
  <main class="register">
    <div class="register-container">
      <h1>Create your account</h1>
      <p class="subtitle">Join our community of pet lovers!</p>

      <form @submit.prevent="handleSubmit" class="register-form">
        <!-- Name Fields -->
        <div class="name-fields">
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input
              type="text"
              id="firstName"
              v-model="formData.firstName"
              :class="{ 'error-input': errors.firstName }"
            />
            <span class="error-message" v-if="errors.firstName">{{ errors.firstName }}</span>
          </div>

          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input
              type="text"
              id="lastName"
              v-model="formData.lastName"
              :class="{ 'error-input': errors.lastName }"
            />
            <span class="error-message" v-if="errors.lastName">{{ errors.lastName }}</span>
          </div>
        </div>

        <!-- Email Field -->
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

        <!-- Password Fields -->
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

        <div class="form-group">
          <label for="confirmPassword">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="formData.confirmPassword"
            :class="{ 'error-input': errors.confirmPassword }"
          />
          <span class="error-message" v-if="errors.confirmPassword">{{
            errors.confirmPassword
          }}</span>
        </div>

        <!-- Terms Checkbox -->
        <div class="form-group checkbox-group">
          <label class="checkbox-label">
            <input
              type="checkbox"
              v-model="formData.agreeTerms"
              :class="{ 'error-input': errors.agreeTerms }"
            />
            <span
              >I agree to the <a href="#" class="link">Terms of Service</a> and
              <a href="#" class="link">Privacy Policy</a></span
            >
          </label>
          <span class="error-message" v-if="errors.agreeTerms">{{ errors.agreeTerms }}</span>
        </div>

        <!-- Submit Button -->
        <button type="submit" class="submit-btn">Create Account</button>

        <!-- Login Link -->
        <p class="login-link">
          Already have an account?
          <a @click="goToLogin" class="link">Log in</a>
        </p>
      </form>
    </div>
  </main>
  <Footer />
</template>

<style scoped>
.register {
  min-height: calc(100vh - 140px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background-color: #f8f9fa;
}

.register-container {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 600px;
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

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.name-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
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

input[type='text'],
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

.checkbox-group {
  margin-top: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.checkbox-label input[type='checkbox'] {
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
  margin-top: 1rem;
}

.submit-btn:hover {
  background-color: #ff6241;
}

.login-link {
  text-align: center;
  margin-top: 1rem;
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
  .register {
    padding: 1rem;
  }

  .register-container {
    padding: 1.5rem;
  }

  .name-fields {
    grid-template-columns: 1fr;
  }

  h1 {
    font-size: 1.75rem;
  }
}
</style>
