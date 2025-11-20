import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

const STORAGE_KEYS = {
  PRIZES: 'nobel-prizes',
  LAUREATES: 'nobel-laureates'
}

const initialPrizes = [
  { id: 1, category: 'Физика', awardDate: '2023-12-10', grantAmount: 10000000 },
  { id: 2, category: 'Химия', awardDate: '2023-12-10', grantAmount: 10000000 },
  { id: 3, category: 'Медицина', awardDate: '2023-12-10', grantAmount: 10000000 }
]

const initialLaureates = [
  { id: 1, name: 'Пьер Кюри', birthDate: '1859-05-15', prizesCount: 1 },
  { id: 2, name: 'Мария Кюри', birthDate: '1867-11-07', prizesCount: 2 },
  { id: 3, name: 'Альберт Эйнштейн', birthDate: '1879-03-14', prizesCount: 1 }
]

const loadFromStorage = (key, defaultValue) => {
  try {
    const item = localStorage.getItem(key)
    return item ? JSON.parse(item) : defaultValue
  } catch (error) {
    console.error(`Ошибка загрузки из localStorage (${key}):`, error)
    return defaultValue
  }
}

const saveToStorage = (key, data) => {
  try {
    localStorage.setItem(key, JSON.stringify(data))
  } catch (error) {
    console.error(`Ошибка сохранения в localStorage (${key}):`, error)
  }
}

export const useDataStore = defineStore('data', () => {
  const prizes = ref(loadFromStorage(STORAGE_KEYS.PRIZES, initialPrizes))
  const laureates = ref(loadFromStorage(STORAGE_KEYS.LAUREATES, initialLaureates))

  watch(prizes, (newPrizes) => {
    saveToStorage(STORAGE_KEYS.PRIZES, newPrizes)
  }, { deep: true })

  watch(laureates, (newLaureates) => {
    saveToStorage(STORAGE_KEYS.LAUREATES, newLaureates)
  }, { deep: true })

  const addPrize = (prizeData) => {
    const newPrize = {
      id: Math.max(...prizes.value.map(p => p.id), 0) + 1,
      ...prizeData
    }
    prizes.value.push(newPrize)
  }

  const addLaureate = (laureateData) => {
    const newLaureate = {
      id: Math.max(...laureates.value.map(l => l.id), 0) + 1,
      ...laureateData
    }
    laureates.value.push(newLaureate)
  }

  const deletePrize = (prizeId) => {
    const index = prizes.value.findIndex(prize => prize.id === prizeId)
    if (index !== -1) {
      prizes.value.splice(index, 1)
    }
  }

  const deleteLaureate = (laureateId) => {
    const index = laureates.value.findIndex(laureate => laureate.id === laureateId)
    if (index !== -1) {
      laureates.value.splice(index, 1)
    }
  }

  const exportData = () => {
    const data = {
      prizes: prizes.value,
      laureates: laureates.value,
      exportedAt: new Date().toISOString()
    }
    return JSON.stringify(data, null, 2)
  }

  const importData = (jsonData) => {
    try {
      const data = JSON.parse(jsonData)
      
      if (data.prizes && Array.isArray(data.prizes)) {
        prizes.value = data.prizes
      }
      
      if (data.laureates && Array.isArray(data.laureates)) {
        laureates.value = data.laureates
      }
      
      return { success: true, message: 'Данные успешно импортированы' }
    } catch (error) {
      return { success: false, message: 'Ошибка при импорте данных: неверный формат JSON' }
    }
  }

  const resetData = () => {
    prizes.value = [...initialPrizes]
    laureates.value = [...initialLaureates]
  }

  const getStats = () => {
    return {
      prizesCount: prizes.value.length,
      laureatesCount: laureates.value.length,
      lastUpdate: new Date().toLocaleString('ru-RU')
    }
  }

  return {
    prizes,
    laureates,
    addPrize,
    addLaureate,
    deletePrize,
    deleteLaureate,
    exportData,
    importData,
    resetData,
    getStats
  }
})