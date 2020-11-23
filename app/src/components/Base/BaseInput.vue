<template>
  <div>
    <label 
      class="block mb-2 text-sm font-bold text-gray-700"
      :for="id">
      {{ label }}
    </label>
    <input
      class="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
      :type="type"
      :id="id"
      :placeholder="placeholder"
      :value="value" 
      @input="$emit('update:value', $event.target.value)">
    </div>
</template>

<script>
export default {
  name: "BaseInput",
  props: {
    label: String,
    placeholder: String,
    value: String,
    type: {
      default: "text",
      type: String
    }
  },
  computed: {
    id() {
      return this.label.toLowerCase().split().join('-')
    }
  }

}
</script>

