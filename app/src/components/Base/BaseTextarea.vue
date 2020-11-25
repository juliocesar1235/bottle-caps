<template>
  <div>
    <label 
      class="block mb-2 text-sm font-bold text-gray-700"
      :for="id">
      {{ label }}
    </label>
    <textarea
      class="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
      :id="id"
      :placeholder="placeholder"
      :value="value" 
      @input="$emit('update:value', $event.target.value)"
      :rows="rows"></textarea>
    </div>
</template>

<script>
export default {
  name: "BaseTextarea",
  props: {
    label: String,
    placeholder: String,
    value: String,
    type: {
      default: "text",
      type: String
    },
    rows: {
      default: 4,
      type: Number
    }
  },
  computed: {
    id() {
      return this.label.toLowerCase().split().join('-')
    }
  }

}
</script>

