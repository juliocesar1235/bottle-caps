<template>
  <section class="pl-4 mb-8 ml-auto mr-auto max-w-screen-xl">
    <h1 class="mb-4 text-3xl text-gray-800">Featured titles</h1>
    <section 
      class="overflow-x-scroll grid grid-flow-col grid-rows-1 gap-4 grid-horizontal-scroll">
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
  <section class="pl-4 ml-auto mr-auto max-w-screen-xl">
    <h1 class="mb-4 text-3xl text-gray-800">All titles</h1>
    <div class="flex mb-4">
      <MultiSelect
        class="mr-4"
        v-model="selectedCategories"
        :options="categories"
        optionLabel="category"
        placeholder="Select categories"
        display="chip"/>
      <BaseButton @click="filter">Filter</BaseButton>
    </div>
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
import BaseButton from '@/components/Base/BaseButton.vue'
import ImageCard from '@/components/ImageCard.vue'
import MultiSelect from 'primevue/multiselect';

export default {
  components: { 
    ImageCard,
    BaseButton,
    MultiSelect
  },
  data() {
    return {
      selectedCategories: [],
      featuredTitles: null
    }
  },
  computed: {
    categories() {
      return this.$store.getters.getCategories.map(category => ({category: category.name, value: category.id}))
    },
    titles() {
      return this.$store.getters.getTitles
    },
  },
  methods: {
    filter() {
      let categories = this.selectedCategories.map(category => category.value)
      this.$store.dispatch('fetchFilteredTitles', {categories})
    }
  },
  mounted() {
    this.$store.dispatch('fetchTitles')
      .then(() => {
        this.featuredTitles = this.$store.getters.getTitles.filter(title => title.featured)
      })
    this.$store.dispatch('fetchCategories')
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
