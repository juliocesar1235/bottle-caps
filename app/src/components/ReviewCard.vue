<template>
  <div class="w-full max-w-md p-4 bg-white rounded-md shadow-md review-grid">
    <header class="mb-2">
      <h3 class="text-xl">{{ heading }}</h3>
    </header>
    <main class="mb-2">
      <p>{{ content }}</p>
    </main>
    <footer class="flex items-center justify-between">
      <star-rating
        :rating="rating"
        :read-only="true"
        :show-rating="false"
        :star-size="25"
        :star-points="[23, 2, 14, 17, 0, 19, 10, 34, 7, 50, 23, 43, 38, 50, 36, 34, 46, 19, 31, 17]"/>
      <p>{{ author }}</p>
    </footer>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: "ReviewCard",
  components: { StarRating },
  props: {
    heading: String,
    content: String,
    author: String,
    rating: Number
  }
};
</script>

<style scopped>
  .review-grid {
    display: grid;
    grid-template-rows: 3rem 1fr 2rem;
  }
</style>