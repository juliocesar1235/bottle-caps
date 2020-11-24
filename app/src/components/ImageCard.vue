<template>
  <div 
    class="inline-block shadow-lg">
    <img
      class="inline-block object-cover object-center w-full h-full"
      :src="url"
      :alt="altText">
  </div>
</template>

<script>
export default {
  name: "ImageCard",
  props: {
    url: String,
    altText: {
      type: String,
      required: false,
      default: "Game cover"
    }
  }
}
</script>