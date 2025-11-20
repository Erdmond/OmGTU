<template>
  <div class="form-overlay" v-if="show" @click.self="close">
    <div class="form-container" @click.stop>
      <div class="form-header">
        <h3>{{ title }}</h3>
        <button class="close-btn" @click="close">×</button>
      </div>
      
      <form @submit.prevent="submit" class="form">
        <div class="form-group" v-for="field in fields" :key="field.key">
          <label :for="field.key">{{ field.label }}</label>
          <input
            :type="field.type || 'text'"
            :id="field.key"
            v-model="formData[field.key]"
            :required="field.required"
            class="form-input"
            :placeholder="field.placeholder || ''"
          >
        </div>
        
        <div class="form-actions">
          <button type="button" class="btn-cancel" @click="close">Отмена</button>
          <button type="submit" class="btn-submit">Добавить</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddForm',
  props: {
    show: Boolean,
    title: String,
    fields: Array
  },
  emits: ['submit', 'update:show'],
  data() {
    return {
      formData: {}
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        this.formData = {}
        this.fields.forEach(field => {
          this.formData[field.key] = field.default || ''
        })
      }
    }
  },
  methods: {
    submit() {
      this.$emit('submit', { ...this.formData })
      this.close()
    },
    close() {
      this.$emit('update:show', false)
    }
  }
}
</script>

<style scoped>
.form-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.form-container {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #f1f3f4;
}

.form-header h3 {
  color: #2c3e50;
  margin: 0;
  font-size: 1.5rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #6c757d;
  line-height: 1;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

.close-btn:hover {
  background: #f8f9fa;
  color: #dc3545;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #2c3e50;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid #f1f3f4;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.btn-cancel:hover {
  background: #5a6268;
  transform: translateY(-1px);
}

.btn-submit {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}
</style>