<template>
  <Navigation />
  <main class="h-full bg-gray-100">
    <router-view/>
  </main>
</template>

<script>
// @ is an alias to /src
import Navigation from "@/components/Navigation.vue";

export default {
  name: "App",
  components: {
    Navigation,
  }
};
</script>

<style lang="scss">
html, body, #app {
  min-height: 100vh;
}

#app {
  display: grid;
  grid-template-areas: "nav" "main";
  grid-template-rows: 4rem 1fr;
}

</style>
