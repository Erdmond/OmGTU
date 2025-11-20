import { createRouter, createWebHistory } from 'vue-router'
import PrizesPage from '@/views/PrizesPage.vue'
import LaureatesPage from '@/views/LaureatesPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'prizes',
      component: PrizesPage
    },
    {
      path: '/laureates',
      name: 'laureates', 
      component: LaureatesPage
    }
  ]
})

export default router