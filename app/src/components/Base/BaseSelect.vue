<template>
  <div>
    <label 
      class="block mb-2 text-sm font-bold text-gray-700"
      :for="id">
      {{ label }}
    </label>
    <select 
      :id="id"
      :value="value" 
      @input="$emit('update:value', $event.target.value)">
      <option 
        v-for="option in options"
        :key="option.id"
        :disabled="option.value === ''"
        :value="option.value">{{ option.label }}</option>  
    </select>
    </div>
</template>

<script>
export default {
  name: "BaseSelect",
  props: {
    label: String,
    options: Array,
    value: [String, Number]
  },
  computed: {
    id() {
      return this.label.toLowerCase().split().join('-')
    }
  }
}
</script>

