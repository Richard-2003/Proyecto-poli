<script setup></script>

<template>
  <header>
    <!-- INCLUIR ICONO -->
    <h1>PetLife</h1>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/categories">Categories</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
    </nav>
  </header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: white;
  color: black;
}

nav {
  display: flex;
  gap: 1rem;
}

a {
  color: black;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s ease;
}

/* Estilo para los enlaces de login y register */
a[href='/login'],
a[href='/register'] {
  background-color: #ff7a5a;
  color: white;
  border: none;
}

/* Efecto hover para login y register */
a[href='/login']:hover,
a[href='/register']:hover {
  background-color: #ff6241;
  transform: translateY(-1px);
}

/* Estilo para cuando el mouse está sobre los otros links */
a:hover {
  border-color: currentColor;
}
</style>
