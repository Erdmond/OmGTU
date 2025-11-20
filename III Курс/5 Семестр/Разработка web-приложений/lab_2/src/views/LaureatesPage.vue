<template>
  <div class="page">
    <h1 class="page-title">Лауреаты</h1>
    
    <button @click="showForm = true" class="add-btn">Добавить лауреата</button>
    
    <div class="table-container">
      <ReusableTable 
        :data="dataStore.laureates" 
        :columns="columns"
        :showDelete="true"
        @delete="deleteLaureate"
      />
    </div>
    
    <AddForm
      v-model:show="showForm"
      title="Добавить лауреата"
      :fields="formFields"
      @submit="handleAddLaureate"
    />
  </div>
</template>

<script>
import { useDataStore } from '@/stores/dataStore'
import ReusableTable from '@/components/ReusableTable.vue'
import AddForm from '@/components/AddForm.vue'

export default {
  name: 'LaureatesPage',
  components: {
    ReusableTable,
    AddForm
  },
  setup() {
    const dataStore = useDataStore()
    return { dataStore }
  },
  data() {
    return {
      showForm: false,
      columns: [
        { key: 'id', title: 'ID' },
        { key: 'name', title: 'Имя/Название' },
        { key: 'birthDate', title: 'Дата рождения/основания' },
        { key: 'prizesCount', title: 'Количество премий' }
      ],
      formFields: [
        { 
          key: 'name', 
          label: 'Имя/Название', 
          required: true,
          placeholder: 'Имя лауреата или название организации'
        },
        { 
          key: 'birthDate', 
          label: 'Дата рождения/основания', 
          type: 'date',
          required: true
        },
        { 
          key: 'prizesCount', 
          label: 'Количество премий', 
          type: 'number',
          required: true,
          placeholder: '1'
        }
      ]
    }
  },
  methods: {
    handleAddLaureate(laureateData) {
      const processedData = {
        ...laureateData,
        prizesCount: parseInt(laureateData.prizesCount)
      }
      this.dataStore.addLaureate(processedData)
      this.showForm = false
    },
    deleteLaureate(laureateId) {
      if (confirm('Удалить этого лауреата?')) {
        this.dataStore.deleteLaureate(laureateId)
      }
    }
  }
}
</script>