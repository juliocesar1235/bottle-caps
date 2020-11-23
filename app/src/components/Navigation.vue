<template>
  <nav class="flex items-center justify-between px-4 py-2 bg-gray-800">
    <p class="text-3xl text-gray-100">Bottle Caps</p>
    <div v-if="logged" class="text-gray-100">
      <p>Logout</p>
    </div>
  </nav>
</template>

<script>

export default {
  data() {
    return {
      logged: false,
    }
  },
  mounted() {
    this.logged = this.$store.getters.getLogged
  }
};
</script>
