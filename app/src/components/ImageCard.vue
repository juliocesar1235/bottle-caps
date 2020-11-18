<template>
  <div :class="[width, height]" class="mb-8 mr-6 shadow-lg">
    <img class="w-full" :src="url" alt="Game cover">
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
    }
  }
}
</script>