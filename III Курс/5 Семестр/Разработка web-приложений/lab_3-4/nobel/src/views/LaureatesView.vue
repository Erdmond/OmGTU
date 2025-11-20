<template>
  <div class="laureates-view">
    <h1>Nobel Laureates</h1>
    
    <div v-if="error" class="error-message">
      <h3>Error loading data:</h3>
      <pre>{{ error }}</pre>
    </div>
    
    <div v-else-if="loading" class="loading">
      Loading laureates...
    </div>
    
    <DataTable
      v-else
      :data="laureates"
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
import DataTable from '@/components/DataTable.vue';
import apiService from '@/services';
import type { Laureate } from '@/services/nobelService';

const laureates = ref<Laureate[]>([]);
const totalCount = ref(0);
const currentPage = ref(1);
const pageSize = ref(10);
const loading = ref(false);
const error = ref<string | null>(null);
const filters = ref({
  birthCountry: '',
  awardYear: '',
});

const fetchLaureates = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    const params = {
      offset: (currentPage.value - 1) * pageSize.value,
      limit: pageSize.value,
      ...(filters.value.birthCountry && { birthCountry: filters.value.birthCountry }),
      ...(filters.value.awardYear && { awardYear: filters.value.awardYear }),
    };

    const response = await apiService.nobel.getLaureates(params);
    laureates.value = response.laureates;
    totalCount.value = response.totalCount;
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Unknown error occurred';
    laureates.value = [];
    totalCount.value = 0;
  } finally {
    loading.value = false;
  }
};

watch([currentPage, pageSize, filters], fetchLaureates, { deep: true });
onMounted(fetchLaureates);
</script>

<style scoped>
.laureates-view {
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
