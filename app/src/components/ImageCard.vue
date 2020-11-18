<template>
  <div :class="[width, height]" class="shadow-lg">
    <img class="w-full" :src="url" :alt="altText">
  </div>
</template>

<script>
export default {
  name: "ImageCard",
  props: {
    url: String,
    width: {
      type: String,
      required: false,
      default: "w-40"
    },
    height: {
      type: String,
      required: false,
      default: "h-41"
    },
    altText: {
      type: String,
      required: false,
      default: "Game cover"
    }
  }
}
</script>