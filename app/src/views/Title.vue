<template>
<Modal v-if="reviewing">
  <template v-slot:header>
    Start review
  </template>
  <template v-slot:content>
    <form>
      <BaseInput
        class="mb-4"
        label="Title"
        placeholder="Amazing game!"
        v-model:value="review.heading"/>
      <BaseTextarea
        class="mb-4"
        label="Content"
        placeholder="This is a great game because..."
        v-model:value="review.comment"
        :rows="6"/>
      <BaseSelect
        class="mb-4"
        label="Rating"
        v-model:value="review.rating"
        :options="options"/>
    </form>
  </template>
  <template v-slot:actions>
    <BaseButton
      @click="publish">Publish</BaseButton>
  </template>
</Modal>
<section class="max-w-screen-xl px-4 mb-8 ml-auto mr-auto">
  <h1 class="mt-4 mb-4 text-3xl text-gray-800">{{ title.name }}</h1>
  <section class="flex flex-col mb-8 md:flex-row">
    <ImageCard
      class="w-full mb-4 lg:w-1/4 md:w-1/2 md:mr-4 md:mb-0"
      :altText="title.name"
      :url="title.cover_image_path"/>
    <div class="flex flex-col items-start justify-between md:w-3/4 md:pb-2">
      <div>
        <h2 class="mb-4 text-2xl">Synopsis</h2>
        <p class="mb-8 leading-loose">{{ title.synopsis }}</p>
      </div>
      <div class="flex items-end justify-between w-full">
        <div>
          <h2 class="text-2xl">User score</h2>
          <star-rating
            :rating="Number(title.user_score)"
            :increment="0.25"
            :read-only="true"
            :star-points="[23, 2, 14, 17, 0, 19, 10, 34, 7, 50, 23, 43, 38, 50, 36, 34, 46, 19, 31, 17]"/>
        </div>
        <BaseButton
          v-if="!title.reviewed"
          :ghost="true"
          @click="() => {reviewing = true}">Review it</BaseButton>
      </div>
    </div>
  </section>
  <section class="flex flex-col justify-between md:flex-row">
    <div class="w-full mb-8 md:w-1/2 lg:w-3/4 lg:mr-0 md:mb-0 md:mr-4">
      <h2 class="mb-4 text-2xl">Reviews</h2>
      <div class="grid grid-cols-1 gap-4 pr-4 lg:grid-cols-2">
        <ReviewCard
          class="mr-2"
          v-for="review in title.reviews"
          :key="review.heading"
          :heading="review.heading"
          :content="review.comment"
          :author="review.author"
          :rating="review.rating"/>
      </div>
    </div>
    <div class="w-full md:w-1/2 lg:w-1/4">
      <h2 class="mb-4 text-2xl">Similar titles</h2>
      <div class="flex">
        <router-link
          replace
          class="contents"
          v-for="related_title in title.related_titles"
          :key="related_title.id"
          :to="{name: 'title', params: {id: related_title.id}}">
          <ImageCard
            class="w-full mr-2 min-w-max"
            :altText="related_title.name"
            :url="related_title.cover_image_path"/>
          </router-link>
      </div>
    </div>
  </section>
</section>
</template>

<script>
import BaseButton from '@/components/Base/BaseButton.vue'
import BaseInput from '@/components/Base/BaseInput.vue'
import BaseSelect from '@/components/Base/BaseSelect.vue'
import BaseTextarea from '@/components/Base/BaseTextarea.vue'
import ImageCard from '@/components/ImageCard.vue'
import ReviewCard from '@/components/ReviewCard.vue'
import Modal from '@/components/Modal.vue'
import StarRating from 'vue-star-rating'

export default {
  name: "Title",
  components: { 
    ImageCard,
    ReviewCard,
    BaseButton,
    BaseInput,
    BaseTextarea,
    BaseSelect,
    Modal,
    StarRating
  },
  data() {
    return {
      reviewing: false,
      review: {
        heading: "",
        comment: "",
        rating: 0,
        title: this.$route.params.id
      }
    }
  },
  computed: {
    title() {
      return this.$store.getters.getCurrentTitle
    },
    options() {
      let o = []
      o.push({id: 0, value: "", label: 'Rate this game'})
      for(let i = 1; i <= 5; i++) {
        o.push({id: i, value: i, label: `${i} stars`})
      }
      return o
    }
  },
  mounted() {
    this.$store.dispatch('fetchTitle', Number(this.$route.params.id))
  },
  beforeRouteUpdate(to, from, next) {
    this.$store.dispatch('fetchTitle', Number(to.params.id))
    next()
  },
  methods: {
    async publish() {
      const data = await this.$store.dispatch('postReview', this.review)
      if(!data.error) {
        this.reviewing = false
        let currentTitle = JSON.parse(JSON.stringify(this.$store.getters.getCurrentTitle))
        currentTitle.reviews.push(data)
        this.$store.commit('setCurrentTitle', currentTitle)
      }
    }
  }
}
</script>

<style>

</style>