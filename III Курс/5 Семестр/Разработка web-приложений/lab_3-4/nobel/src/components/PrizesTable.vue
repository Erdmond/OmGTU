<template>
  <div class="prizes-table">
    <div class="filters">
      <input
        :value="filters.year"
        placeholder="Filter by year"
        @input="updateYear($event)"
      />
      <input
        :value="filters.category"
        placeholder="Filter by category"
        @input="updateCategory($event)"
      />
    </div>

    <table>
      <thead>
        <tr>
          <th>Year</th>
          <th>Category</th>
          <th>Date Awarded</th>
          <th>Prize Amount</th>
          <th>Laureates</th>
          <th>Motivation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="prize in data" :key="`${prize.awardYear}-${prize.category?.en}`">
          <td>{{ prize.awardYear }}</td>
          <td>{{ prize.category?.en }}</td>
          <td>{{ formatDate(prize.dateAwarded) }}</td>
          <td>{{ formatPrizeAmount(prize.prizeAmount) }}</td>
          <td>
            <div v-for="laureate in prize.laureates" :key="laureate.id">
              {{ laureate.fullName?.en }}
            </div>
          </td>
          <td>
            <div v-for="laureate in prize.laureates" :key="laureate.id">
              {{ truncateText(laureate.motivation?.en, 30) }}
            </div>
          </td>
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
import { computed } from 'vue';
import type { Prize } from '@/services/nobelService';

interface Props {
  data: Prize[];
  totalItems: number;
  currentPage: number;
  pageSize: number;
  filters: {
    year: string;
    category: string;
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

const updateYear = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const value = target?.value || '';
  
  const newFilters = {
    ...props.filters,
    year: value
  };
  emit('update:filters', newFilters);
  emit('update:currentPage', 1);
};

const updateCategory = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const value = target?.value || '';
  
  const newFilters = {
    ...props.filters,
    category: value
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

const formatPrizeAmount = (amount?: number): string => {
  if (!amount) return 'N/A';
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'SEK'
  }).format(amount);
};

const truncateText = (text?: string, maxLength: number = 50): string => {
  if (!text) return 'N/A';
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};
</script>

<style scoped>
.prizes-table {
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
</style>
