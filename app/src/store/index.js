import { createStore } from "vuex";

export default createStore({
  state: {
    user: {
      username: "Sergio"
    },
    logged: false
  },
  mutations: { // sync
    setUser(state, payload) {
      state.user = payload
    },
    setLogged(state, payload) {
      state.logged = payload
    }
  },
  actions: { // async

  },
  modules: {},
  getters: {
    getUser: state => state.user,
    getLogged: state => state.logged
  }
});
