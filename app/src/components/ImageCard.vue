<template>
  <div 
    class="object-cover object-center shadow-lg">
    <img
      class="object-cover object-center w-full h-full"
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