<template>
  <header>
    <Navigation />
  </header>
  <main class="h-full bg-gray-100">
    <router-view/>
  </main>
  <footer class="bg-gray-100"></footer>
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
  grid-template-areas: "nav" "main" "footer";
  grid-template-rows: 4rem 1fr 4rem;
}

</style>
