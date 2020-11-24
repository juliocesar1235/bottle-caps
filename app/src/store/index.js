import { createStore } from "vuex";

const url = "http://localhost:8000"

export default createStore({
  state: {
    user: {},
    isAuthenticated: localStorage.getItem('token') ? true : false,
    titles: []
  },
  mutations: { // sync
    setUser(state, payload) {
      state.user = payload
    },
    setIsAuthenticated(state, payload) {
      state.isAuthenticated = payload
    },
    setTitles(state, payload) {
      state.titles = payload
    }
  },
  actions: { // async
    async login(state, payload) {
      const options = {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      }
      const res = await fetch(`${url}/login/`, options)
      if(res.ok) {
        const token = await res.json()
        state.commit('setIsAuthenticated', true)
        localStorage.setItem('token', token.token)
        return {}
      } else {
        return {error: "Wrong credentials"}
      }
    },
    async fetchTitles(state) {
      const options = {
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
      }
      const res = await fetch(`${url}/titles/`, options)
      if(res.ok) {
        const titles = await res.json()
        state.commit('setTitles', titles)
        return {}
      } else {
        return {error: "Something wrong happened. Please try again later!"}
      }
    }
  },
  modules: {},
  getters: {
    getUser: state => state.user,
    isAuthenticated: state => state.isAuthenticated,
    getTitles: state => state.titles
  }
});
