<template>
  <div class="page">
    <h1 class="page-title">Нобелевские премии</h1>
    
    <button @click="showForm = true" class="add-btn">Добавить премию</button>
    
    <div class="table-container">
      <ReusableTable 
        :data="dataStore.prizes" 
        :columns="columns"
        :showDelete="true"
        @delete="deletePrize"
      />
    </div>
    
    <AddForm
      v-model:show="showForm"
      title="Добавить премию"
      :fields="formFields"
      @submit="handleAddPrize"
    />
  </div>
</template>

<script>
import { useDataStore } from '@/stores/dataStore'
import ReusableTable from '@/components/ReusableTable.vue'
import AddForm from '@/components/AddForm.vue'

export default {
  name: 'PrizesPage',
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
        { key: 'category', title: 'Категория' },
        { key: 'awardDate', title: 'Дата вручения' },
        { key: 'grantAmount', title: 'Размер гранта' }
      ],
      formFields: [
        { 
          key: 'category', 
          label: 'Категория', 
          required: true,
          placeholder: 'Физика, Химия, Литература...'
        },
        { 
          key: 'awardDate', 
          label: 'Дата вручения', 
          type: 'date',
          required: true
        },
        { 
          key: 'grantAmount', 
          label: 'Размер гранта', 
          type: 'number',
          required: true,
          placeholder: '10000000'
        }
      ]
    }
  },
  methods: {
    handleAddPrize(prizeData) {
      const processedData = {
        ...prizeData,
        grantAmount: parseFloat(prizeData.grantAmount)
      }
      this.dataStore.addPrize(processedData)
      this.showForm = false
    },
    deletePrize(prizeId) {
      if (confirm('Удалить эту премию?')) {
        this.dataStore.deletePrize(prizeId)
      }
    }
  }
}
</script>