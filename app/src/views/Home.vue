<template>
  <section class="max-w-screen-xl pl-4 mb-8 ml-auto mr-auto">
    <h1 class="mb-4 text-3xl text-gray-800">Featured titles</h1>
    <section 
      class="grid grid-flow-col grid-rows-1 gap-4 overflow-x-scroll grid-horizontal-scroll">
      <router-link
        class="contents"
        :to="{name: 'title', params: {id: title.id}}"
        v-for="title in featuredTitles"
        :key="title.id">
        <ImageCard
          :key="title.id" 
          :altText="title.name" 
          :url="title.cover_image_path"/>
      </router-link>
    </section>
  </section>
  <section class="max-w-screen-xl pl-4 ml-auto mr-auto">
    <h1 class="mb-4 text-3xl text-gray-800">All titles</h1>
    <section 
      class="grid grid-cols-2 gap-4 lg:grid-cols-6 md:grid-cols-4">
      <router-link 
        class="contents"
        :to="{name: 'title', params: {id: title.id}}"
        v-for="title in titles"
        :key="title.id">
        <ImageCard
          :key="title.id" 
          :altText="title.name" 
          :url="title.cover_image_path"/>
      </router-link>
    </section>
  </section>
</template>

<script>
import ImageCard from '../components/ImageCard.vue'
export default {
  components: { ImageCard },
  computed: {
    titles() {
      return this.$store.getters.getTitles
    },
    featuredTitles() {
      return this.titles.filter(title => title.featured)
    }
  },
  mounted() {
    this.$store.dispatch('fetchTitles')
  }

}
</script>

<style scoped>
  .grid-horizontal-scroll {
    grid-template-columns: repeat(2, 50%);
    grid-auto-columns: 50%;
    position: relative;
  }

  .grid-horizontal-scroll::-webkit-scrollbar {
    display: none;
  }

  @media screen and (min-width: 768px){
    .grid-horizontal-scroll {
      grid-template-columns: repeat(4, 25%);
      grid-auto-columns: 25%;
    }
  }

  @media screen and (min-width: 1024px){
    .grid-horizontal-scroll {
      grid-template-columns: repeat(8, 12.5%);
      grid-auto-columns: 16%;
    }
  }
</style>