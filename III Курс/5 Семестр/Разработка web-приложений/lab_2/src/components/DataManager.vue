<template>
  <div class="data-manager">
    <button @click="$emit('open-manager')" class="manager-btn" title="Управление данными">
      Управление данными
    </button>
  </div>
</template>

<script>
export default {
  name: 'DataManager',
  emits: ['open-manager']
}
</script>

<style scoped>
.data-manager {
  display: inline-block;
}

.manager-btn {
  padding: 0.5rem 1rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.2s ease;
}

.manager-btn:hover {
  background: #545b62;
}
</style>