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
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
    component: ()=> import('../views/Register.vue')
    },
    {
     path: '/login',
     name: 'login',
     component: ()=> import('../views/LoginView.vue') 
    },
    {
      path: '/explore',
      name: 'explore',
      component: ()=> import('../views/Explore.vue')
    },
    {
      path: '/cars/new',
      name: 'add car',
      component: ()=> import('../views/AddCar.vue')
    },
    {
      path: '/cars/:car_id',
      name: 'car view',
      component: ()=>import ('../views/CarView.vue')
    },

    {
      path: '/logout',
      name: 'logout',
      component: ()=> import('../views/Logout.vue')
    },

    {
      path: '/users/:user_id',
      name: 'profile',
      component: ()=> import('../views/Profile.vue')
    }
    
  ]
});

export default router
