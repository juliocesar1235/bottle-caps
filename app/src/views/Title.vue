<template>
<section class="max-w-screen-xl px-4 mb-8 ml-auto mr-auto">
  <h1 class="mt-4 mb-4 text-3xl text-gray-800">{{ title.name }}</h1>
  <section class="flex flex-col items-start mb-8 lg:flex-row">
    <ImageCard
      class="w-full mb-4 lg:w-1/4 md:mr-4 lg:mb-0"
      :altText="title.name"
      :url="title.cover_image_path"/>
    <div class="flex flex-col items-start justify-between lg:w-3/4">
      <div>
        <h2 class="mb-4 text-2xl">Synopsis</h2>
        <p class="mb-8 leading-loose">{{ title.synopsis }}</p>
      </div>
      <div>
        <h2 class="text-2xl">User score</h2>
        <star-rating 
          :rating="Number(title.user_score)"
          :round-start-rating="false"
          :read-only="true"
          :star-points="[23, 2, 14, 17, 0, 19, 10, 34, 7, 50, 23, 43, 38, 50, 36, 34, 46, 19, 31, 17]"/>
      </div>
    </div>
  </section>
  <section class="flex flex-col justify-between lg:flex-row">
    <div class="w-4/5 mb-4 lg:mb-0">
      <h2 class="text-2xl">Reviews</h2>
    </div>
    <div class="w-1/5">
      <h2 class="text-2xl">Similar titles</h2>
    </div>
  </section>
</section>
</template>

<script>
import ImageCard from '../components/ImageCard.vue'
import StarRating from 'vue-star-rating'

export default {
  components: { ImageCard, StarRating },
  computed: {
    title() {
      return this.$store.getters.getCurrentTitle
    }
  },
  mounted() {
    this.$store.dispatch('fetchTitle', Number(this.$route.params.id))
  }
}
</script>

<style>

</style>