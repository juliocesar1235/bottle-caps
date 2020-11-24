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
    meta: {title: 'Login | Bottlecaps'}
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
    meta: {title: 'Signup | Bottlecaps'}
  },
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {title: 'Bottlecaps'}
  }
];

const pageTitle = to => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title)
  
  if(nearestWithTitle) document.title = nearestWithTitle.meta.title
  else document.title = "Bottlecaps"
}

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, _, next) => {
  let isAuthenticated = store.getters.isAuthenticated
  if (to.name !== 'login' && to.name !== 'signup' && !isAuthenticated) next({ name: 'login' })
  else if ((to.name === 'login' || to.name === 'signup') && isAuthenticated) next({ name: 'home' })
  else next()
  pageTitle(to)
})

export default router;
