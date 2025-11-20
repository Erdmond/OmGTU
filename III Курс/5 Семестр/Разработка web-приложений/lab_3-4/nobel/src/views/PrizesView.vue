<template>
  <div class="prizes-view">
    <h1>Nobel Prizes</h1>
    
    <div v-if="error" class="error-message">
      <h3>Error loading data:</h3>
      <pre>{{ error }}</pre>
    </div>
    
    <div v-else-if="loading" class="loading">
      Loading prizes...
    </div>
    
    <PrizesTable
      v-else
      :data="prizes"
      :total-items="totalCount"
      :current-page="currentPage"
      :page-size="pageSize"
      :filters="filters"
      @update:current-page="currentPage = $event"
      @update:page-size="pageSize = $event"
      @update:filters="filters = $event"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import PrizesTable from '@/components/PrizesTable.vue';
import apiService from '../services';
import type { Prize } from '@/services/nobelService';

const prizes = ref<Prize[]>([]);
const totalCount = ref(0);
const currentPage = ref(1);
const pageSize = ref(10);
const loading = ref(false);
const error = ref<string | null>(null);
const filters = ref({
  year: '',
  category: '',
});

const fetchPrizes = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    const params = {
      offset: (currentPage.value - 1) * pageSize.value,
      limit: pageSize.value,
      ...(filters.value.year && { year: filters.value.year }),
      ...(filters.value.category && { category: filters.value.category }),
    };

    const response = await apiService.nobel.getPrizes(params);
    prizes.value = response.prizes;
    totalCount.value = response.totalCount;
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Unknown error occurred';
    prizes.value = [];
    totalCount.value = 0;
  } finally {
    loading.value = false;
  }
};

watch([currentPage, pageSize, filters], fetchPrizes, { deep: true });
onMounted(fetchPrizes);
</script>

<style scoped>
.prizes-view {
  padding: 0;
}

h1 {
  color: #2c3e50;
  margin-bottom: 20px;
  text-align: center;
  font-size: 2.5rem;
}

.error-message {
  background: #ffe6e6;
  border: 1px solid #ffcccc;
  border-radius: 4px;
  padding: 15px;
  margin: 20px 0;
  color: #cc0000;
}

.error-message pre {
  white-space: pre-wrap;
  font-size: 12px;
}

.loading {
  text-align: center;
  padding: 40px;
  font-size: 18px;
  color: #666;
}
</style>
