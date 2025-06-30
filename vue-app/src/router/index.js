import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AppLogin from '../views/AppLogin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: AppLogin
  },
  {
    path: '/about',
    name: 'about',
    component: function () {
      return import('../views/AboutView.vue')
    }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: function () {
      return import('../views/DashBoard.vue')
    }
  },
  {
    path: '/newcard',
    name: 'newcard',
    component: function () {
      return import('../views/NewCard.vue')
    }
  },
  {
    path: '/newdeck',
    name: 'newdeck',
    component: function () {
      return import('../views/NewDeck.vue')
    }
  },
  {
    path: '/newuser',
    name: 'newuser',
    component: function () {
      return import('../views/NewUser.vue')
    }
  },
  {
    path: '/deluser',
    name: 'deluser',
    component: function () {
      return import('../views/DeleteUser.vue')
    }
  },
  {
    path: '/reviewdeck',
    name: 'reviewdeck',
    component: function () {
      return import('../views/ReviewDeck.vue')
    }
  },
  {
    path: '/delcard',
    name: 'delcard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/DelCard.vue')
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
