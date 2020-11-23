<template>
  <button
    type="button"
    class="inline-block text-white transition duration-200 rounded-md select-none ease focus:outline-none focus:shadow-outline"
    :class="buttonStyle">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: "indigo"
    },
    ghost: {
      type: Boolean,
      default: false
    },
    flat: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    buttonStyle() {
      const commonClass = "px-4 py-2 border border-${this.color}-500"
      if (this.ghost) {
        return `${commonClass} hover:bg-${this.color}-500 text-${this.color}-500 hover:text-white`  
      } else if (this.flat) {
        return `text-${this.color}-500 hover:underline`  
      }
      return `${commonClass} bg-${this.color}-500 hover:bg-${this.color}-600`
    }
  }
}
</script>

<style>

</style>