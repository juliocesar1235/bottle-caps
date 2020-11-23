import { createRouter, createWebHistory } from "vue-router";
import Signup from "../views/Signup.vue";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";
import store from '../store'

const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {title: 'Login'}
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
    meta: {title: 'Signup'}
  },
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {title: 'Home'}
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, _, next) => {
  let isAuthenticated = store.getters.getLogged
  if (to.name !== 'login' && to.name !== 'signup' && !isAuthenticated) next({ name: 'login' })
  else next()
})

export default router;
