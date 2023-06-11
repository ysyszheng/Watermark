import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    {
      path: '/history',
      name: 'history',
      component: () => import('../views/HistoryView.vue')
    },
    {
      path: '/addwm',
      name: 'addwatermark',
      component: () => import('../views/AddWatermarkView.vue')
    },
    {
      path: '/rmwm',
      name: 'rmwatermark',
      component: () => import('../views/RmWatermarkView.vue')
    },
    {
      path: '/addsg',
      name: 'addsteganography',
      component: () => import('../views/AddSteganographyView.vue')
    },
    {
      path: '/rmsg',
      name: 'rmsteganography',
      component: () => import('../views/RmSteganographyView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue')
    }
  ]
})

export default router
