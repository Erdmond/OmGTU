<template>
  <div id="app">
    <nav>
      <router-link to="/">Nobel Prize Database</router-link>
    </nav>
    <main class="container">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f5f5f5;
}

#app {
  min-height: 100vh;
}

nav {
  background: #2c3e50;
  padding: 1rem;
  margin-bottom: 2rem;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2rem;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}
</style>
