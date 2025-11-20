<template>
  <table class="table">
    <thead>
      <tr>
        <th v-for="column in columns" :key="column.key">
          {{ column.title }}
        </th>
        <th v-if="showDelete">Действия</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in data" :key="item.id">
        <td v-for="column in columns" :key="column.key">
          {{ item[column.key] }}
        </td>
        <td v-if="showDelete">
          <button @click="deleteItem(item.id)" class="delete-btn" title="Удалить">
            🗑️
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'ReusableTable',
  props: {
    data: {
      type: Array,
      required: true
    },
    columns: {
      type: Array,
      required: true
    },
    showDelete: {
      type: Boolean,
      default: false
    }
  },
  emits: ['delete'],
  methods: {
    deleteItem(id) {
      this.$emit('delete', id)
    }
  }
}
</script>

<style scoped>
.delete-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  padding: 0.5rem;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.delete-btn:hover {
  background: #ffe6e6;
}
</style>