<template>
  <div class="data-table">
    <div class="filters">
      <input
        :value="filters.birthCountry"
        placeholder="Filter by country"
        @input="updateBirthCountry($event)"
      />
      <input
        :value="filters.awardYear"
        placeholder="Filter by year"
        @input="updateAwardYear($event)"
      />
    </div>

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Birth Country</th>
          <th>Birth Date</th>
          <th>Award Year</th>
          <th>Category</th>
          <th>Motivation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="laureate in data" :key="laureate.id">
          <td>{{ laureate.fullName?.en }}</td>
          <td>{{ laureate.birth?.place?.country?.en }}</td>
          <td>{{ formatDate(laureate.birth?.date) }}</td>
          <td>{{ laureate.nobelPrizes?.[0]?.awardYear }}</td>
          <td>{{ laureate.nobelPrizes?.[0]?.category?.en }}</td>
          <td>{{ truncateText(laureate.nobelPrizes?.[0]?.motivation?.en, 50) }}</td>
        </tr>
      </tbody>
    </table>

    <div class="pagination">
      <button 
        :disabled="currentPage === 1" 
        @click="changePage(currentPage - 1)"
      >
        Previous
      </button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button 
        :disabled="currentPage >= totalPages" 
        @click="changePage(currentPage + 1)"
      >
        Next
      </button>
      <select :value="pageSize" @change="onPageSizeChange($event)">
        <option value="10">10 per page</option>
        <option value="25">25 per page</option>
        <option value="50">50 per page</option>
      </select>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, defineProps, defineEmits } from 'vue';
import type { Laureate } from '@/services/nobelService';

interface Props {
  data: Laureate[];
  totalItems: number;
  currentPage: number;
  pageSize: number;
  filters: {
    birthCountry: string;
    awardYear: string;
  };
}

interface Emits {
  (e: 'update:currentPage', page: number): void;
  (e: 'update:pageSize', size: number): void;
  (e: 'update:filters', filters: Props['filters']): void;
}

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

const totalPages = computed(() => 
  Math.ceil(props.totalItems / props.pageSize)
);

const updateBirthCountry = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const value = target?.value || '';
  
  const newFilters = {
    ...props.filters,
    birthCountry: value
  };
  emit('update:filters', newFilters);
  emit('update:currentPage', 1);
};

const updateAwardYear = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const value = target?.value || '';
  
  const newFilters = {
    ...props.filters,
    awardYear: value
  };
  emit('update:filters', newFilters);
  emit('update:currentPage', 1);
};

const changePage = (page: number) => {
  emit('update:currentPage', page);
};

const onPageSizeChange = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  const value = target?.value || '10';
  const newSize = parseInt(value, 10);
  
  emit('update:pageSize', newSize);
  emit('update:currentPage', 1);
};

const formatDate = (dateString?: string): string => {
  if (!dateString) return 'N/A';
  try {
    return new Date(dateString).toLocaleDateString();
  } catch {
    return dateString;
  }
};

const truncateText = (text?: string, maxLength: number = 50): string => {
  if (!text) return 'N/A';
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};
</script>

<style scoped>
.data-table {
  margin: 20px 0;
}

.filters {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.filters input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  min-width: 200px;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

th, td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

th {
  background-color: #2c3e50;
  color: white;
  font-weight: 600;
}

tr:hover {
  background-color: #f8f9fa;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 10px;
}

.pagination button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: white;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.pagination button:hover:not(:disabled) {
  background: #2c3e50;
  color: white;
}

.pagination button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.error-message {
  background: #fff3f3;
  border: 1px solid #ffcdd2;
  border-radius: 4px;
  padding: 10px;
  margin: 10px 0;
  color: #d32f2f;
}

.validation-warning {
  background: #fff8e1;
  border: 1px solid #ffecb3;
  border-radius: 4px;
  padding: 10px;
  margin: 10px 0;
  color: #ff8f00;
}

</style>
