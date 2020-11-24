<template>
  <nav class="flex items-center justify-between px-8 py-2 bg-gray-800">
    <p class="text-3xl text-gray-100">Bottle Caps</p>
    <div v-if="logged" class="text-gray-100">
      <router-link @click="logout" :to="{name:'login'}">
        Logout
      </router-link>
    </div>
  </nav>
</template>

<script>

export default {
  name: "Navigation",
  computed: {
    logged() {return this.$store.getters.isAuthenticated}
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
    }
  }
};
</script>
