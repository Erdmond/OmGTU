<template>
  <div class="home-view">
    <div class="tabs">
      <button 
        class="tab" 
        :class="{ active: $route.name === 'laureates' }"
        @click="switchView('laureates')"
      >
        <span class="tab-icon">🏆</span>
        <span class="tab-text">Laureates</span>
      </button>
      <button 
        class="tab" 
        :class="{ active: $route.name === 'prizes' }"
        @click="switchView('prizes')"
      >
        <span class="tab-icon">💰</span>
        <span class="tab-text">Prizes</span>
      </button>
    </div>

    <div class="tab-content">
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

type ViewType = 'laureates' | 'prizes';

const switchView = (view: ViewType) => {
  router.push({ name: view });
};
</script>

<style scoped>
.home-view {
  padding: 20px;
}

.tabs {
  display: flex;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 4px;
  margin-bottom: 30px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.tab {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border: none;
  background: transparent;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: #6c757d;
  transition: all 0.3s ease;
  flex: 1;
  justify-content: center;
}

.tab:hover {
  color: #2c3e50;
  background: rgba(44, 62, 80, 0.05);
}

.tab.active {
  background: white;
  color: #2c3e50;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.tab-icon {
  font-size: 16px;
}

.tab-text {
  white-space: nowrap;
}

.tab-content {
  min-height: 500px;
}
</style>
