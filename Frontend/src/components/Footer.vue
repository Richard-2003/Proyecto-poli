<script setup></script>

<template>
  <footer>
    <p>&copy; 2025 PetLife. All rights reserved.</p>
    <div class="social-icons">
      <a href="https://facebook.com" target="_blank" aria-label="Facebook">
        <i class="fab fa-facebook"></i>
      </a>
      <a href="https://twitter.com" target="_blank" aria-label="X (Twitter)">
        <i class="fab fa-x-twitter"></i>
      </a>
      <a href="https://instagram.com" target="_blank" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
      </a>
    </div>
  </footer>
</template>

<style scoped>
footer {
  padding: 1rem;
  background-color: white;
  color: black;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.social-icons {
  display: flex;
  gap: 1rem;
}

.social-icons a {
  color: #333;
  font-size: 1.5rem;
  transition: color 0.3s ease;
}

.social-icons a:hover {
  color: #ff7a5a;
}

/* Estilos específicos para cada red social al hacer hover */
.fa-facebook:hover {
  color: #1877f2;
}

.fa-x-twitter:hover {
  color: #000000;
}

.fa-instagram:hover {
  color: #e4405f;
}
</style>
