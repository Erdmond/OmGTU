<template>
  <div id="app">
    <header class="header">
      <div class="header-content">
        <h1 class="logo">Нобелевские премии</h1>
        <div class="header-right">
          <nav class="navigation">
            <router-link to="/" class="nav-btn">Премии</router-link>
            <router-link to="/laureates" class="nav-btn">Лауреаты</router-link>
          </nav>
          <DataManager @open-manager="showDataManager = true" />
        </div>
      </div>
    </header>

    <main class="main">
      <div class="container">
        <router-view />
      </div>
    </main>

    <div class="manager-overlay" v-if="showDataManager" @click.self="showDataManager = false">
      <div class="manager-container">
        <div class="manager-header">
          <h3>Управление данными</h3>
          <button class="close-btn" @click="showDataManager = false">×</button>
        </div>

        <div class="manager-content">
          <div class="stats">
            <h4>Статистика</h4>
            <div class="stats-info">
              <div>Премий: <strong>{{ dataStats.prizesCount }}</strong></div>
              <div>Лауреатов: <strong>{{ dataStats.laureatesCount }}</strong></div>
              <div>Обновлено: <strong>{{ dataStats.lastUpdate }}</strong></div>
            </div>
          </div>

          <div class="actions">
            <button @click="handleExport" class="btn export">Экспорт в JSON</button>
            <label class="btn import">
              Импорт из JSON
              <input type="file" @change="handleImport" accept=".json" hidden>
            </label>
            <button @click="handleReset" class="btn reset">Сбросить данные</button>
          </div>

          <div v-if="dataMessage" :class="['message', messageType]">
            {{ dataMessage }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useDataStore } from '@/stores/dataStore'
import DataManager from '@/components/DataManager.vue'

export default {
  name: 'App',
  components: {
    DataManager
  },
  data() {
    return {
      showDataManager: false,
      dataMessage: '',
      messageType: 'info'
    }
  },
  computed: {
    dataStats() {
      const dataStore = useDataStore()
      return dataStore.getStats()
    }
  },
  methods: {
    handleExport() {
      const dataStore = useDataStore()
      const data = dataStore.exportData()
      const blob = new Blob([data], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `nobel-data-${new Date().toISOString().split('T')[0]}.json`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
      
      this.showDataMessage('Данные успешно экспортированы!', 'success')
    },

    handleImport(event) {
      const file = event.target.files[0]
      if (!file) return

      const reader = new FileReader()
      reader.onload = (e) => {
        const dataStore = useDataStore()
        const result = dataStore.importData(e.target.result)
        if (result.success) {
          this.showDataMessage(result.message, 'success')
          event.target.value = ''
        } else {
          this.showDataMessage(result.message, 'error')
        }
      }
      reader.readAsText(file)
    },

    handleReset() {
      if (confirm('Сбросить все данные к исходным?')) {
        const dataStore = useDataStore()
        dataStore.resetData()
        this.showDataMessage('Данные сброшены!', 'success')
      }
    },

    showDataMessage(text, type) {
      this.dataMessage = text
      this.messageType = type
      setTimeout(() => {
        this.dataMessage = ''
      }, 3000)
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background: #f8f9fa;
  color: #212529;
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: #fff;
  border-bottom: 1px solid #dee2e6;
  padding: 1rem 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  color: #212529;
  font-size: 1.5rem;
  font-weight: 600;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.navigation {
  display: flex;
  gap: 0.5rem;
}

.nav-btn {
  padding: 0.5rem 1rem;
  color: #495057;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.2s ease;
  font-weight: 500;
}

.nav-btn:hover {
  background: #e9ecef;
  color: #212529;
}

.nav-btn.router-link-active {
  background: #007bff;
  color: white;
}

.main {
  flex: 1;
  padding: 2rem 0;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
}

.page {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.page-title {
  color: #212529;
  margin-bottom: 1.5rem;
  font-size: 1.75rem;
  font-weight: 600;
  text-align: center;
}

.add-btn {
  margin: 1rem 0;
  padding: 0.75rem 1.5rem;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background-color 0.2s ease;
}

.add-btn:hover {
  background: #0056b3;
}

.table-container {
  margin-top: 1.5rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  overflow: hidden;
}

.table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}

.table th {
  background: #f8f9fa;
  color: #495057;
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  border-bottom: 1px solid #dee2e6;
}

.table td {
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
  color: #212529;
}

.table tr:last-child td {
  border-bottom: none;
}

.table tr:hover {
  background: #f8f9fa;
}

.delete-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #dc3545;
  padding: 0.25rem 0.5rem;
  border-radius: 2px;
}

.delete-btn:hover {
  background: #f8d7da;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 1rem;
  }

  .header-right {
    flex-direction: column;
    gap: 1rem;
  }

  .container {
    padding: 0 1rem;
  }

  .page {
    padding: 1.5rem;
  }
}

.manager-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}

.manager-container {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 450px;
  max-height: 80vh;
  overflow-y: auto;
}

.manager-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #dee2e6;
}

.manager-header h3 {
  color: #212529;
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6c757d;
  padding: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}

.close-btn:hover {
  background: #f8f9fa;
  color: #dc3545;
}

.manager-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.stats {
  background: #f8f9fa;
  padding: 1.25rem;
  border-radius: 6px;
  border-left: 4px solid #007bff;
}

.stats h4 {
  margin: 0 0 0.75rem 0;
  color: #212529;
  font-size: 1rem;
  font-weight: 600;
}

.stats-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: #6c757d;
}

.stats-info div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.25rem 0;
}

.stats-info strong {
  color: #212529;
  font-weight: 600;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.btn {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
  font-size: 0.9rem;
  text-align: center;
}

.export {
  background: #28a745;
  color: white;
}

.export:hover {
  background: #218838;
}

.import {
  background: #17a2b8;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.import:hover {
  background: #138496;
}

.reset {
  background: #dc3545;
  color: white;
}

.reset:hover {
  background: #c82333;
}

.message {
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
  font-weight: 500;
  font-size: 0.9rem;
}

.message.success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.message.error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.message.info {
  background: #d1ecf1;
  color: #0c5460;
  border: 1px solid #bee5eb;
}

@media (max-width: 480px) {
  .manager-container {
    padding: 1.5rem;
    margin: 1rem;
    width: calc(100% - 2rem);
  }
  
  .manager-header h3 {
    font-size: 1.1rem;
  }
  
  .btn {
    padding: 0.9rem 1rem;
  }
  
  .stats {
    padding: 1rem;
  }
}
</style>