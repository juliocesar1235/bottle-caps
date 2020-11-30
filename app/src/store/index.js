import { createStore } from "vuex";

const url = "http://localhost:8000"

export default createStore({
  state: {
    user: {},
    isAuthenticated: localStorage.getItem('token') ? true : false,
    categories: [],
    titles: [],
    currentTitle: {}
  },
  mutations: { // sync
    setUser(state, payload) {
      state.user = payload
    },
    setIsAuthenticated(state, payload) {
      state.isAuthenticated = payload
    },
    setCategories(state, payload) {
      state.categories = payload
    },
    setTitles(state, payload) {
      state.titles = payload
    },
    setCurrentTitle(state, payload) {
      state.currentTitle = payload
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
    async signup(state, payload) {
      const options = {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      }
      const res = await fetch(`${url}/signup/`, options)
      if(res.ok) {
        const token = await res.json()
        state.commit('setIsAuthenticated', true)
        localStorage.setItem('token', token.token)
        return {}
      } else {
        return {error: "Wrong credentials"}
      }
    },
    async fetchCategories(state) {
      const options = {
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
      }
      const res = await fetch(`${url}/categories/`, options)
      if(res.ok) {
        const categories = await res.json()
        state.commit('setCategories', categories)
        return {}
      } else {
        return {error: "Something wrong happened. Please try again later!"}
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
    },
    async fetchFilteredTitles(state, payload) {
      const options = {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(payload)
      }
      const res = await fetch(`${url}/titles-filter/`, options)
      if(res.ok) {
        const titles = await res.json()
        state.commit('setTitles', titles)
        return {}
      } else {
        return {error: "Something wrong happened. Please try again later!"}
      }
    },
    async fetchTitle(state, id) {
      const options = {
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
      }
      const res = await fetch(`${url}/title/${id}/`, options)
      if(res.ok) {
        const title = await res.json()
        state.commit('setCurrentTitle', title)
        return {}
      } else {
        return {error: "Something wrong happened. Please try again later!"}
      }
    },
    async postReview(_, payload) {
      const options = {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(payload)
      }
      const res = await fetch(`${url}/reviews/`, options)
      if(res.ok) {
        return await res.json()
      } else {
        return {error: "Something wrong happened. Please try again later!"}
      }
    }
  },
  modules: {},
  getters: {
    getUser: state => state.user,
    isAuthenticated: state => state.isAuthenticated,
    getCategories: state => state.categories,
    getTitles: state => state.titles,
    getCurrentTitle: state => state.currentTitle
  }
});
