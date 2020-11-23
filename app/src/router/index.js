import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";
import store from '../store'

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {title: 'Login'}
  },
  {
    path: "/",
    name: "Home",
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
  if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
  else next()
})

export default router;
