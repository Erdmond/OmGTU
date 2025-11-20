import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LaureatesView from '../views/LaureatesView.vue';
import PrizesView from '../views/PrizesView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    redirect: '/laureates',
    children: [
      {
        path: 'laureates',
        name: 'laureates',
        component: LaureatesView
      },
      {
        path: 'prizes',
        name: 'prizes',
        component: PrizesView
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
