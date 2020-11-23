<template>
    <div
    class="w-full max-w-md p-4 mt-24 ml-auto mr-auto bg-white shadow-lg">
      <form>
        <BaseInput 
          class="mb-4"
          label="Username"
          placeholder="Username"
          v-model:value="username"/>
        <BaseInput 
          class="mb-4"
          label="Password"
          placeholder="Password"
          v-model:value="password"
          type="password"/>
        <BaseInput 
          class="mb-4"
          label="Confirm password"
          placeholder="Repeat password"
          v-model:value="confirmPassword"
          type="password"/>
        <div class="flex items-center justify-between">
          <router-link :to="{name: 'login'}">
            <BaseButton :flat="true">Back to login</BaseButton>
          </router-link>
          <BaseButton>Create account</BaseButton>
        </div>
      </form>
  </div>
</template>

<script>
import BaseInput from "@/components/Base/BaseInput.vue"
import BaseButton from "@/components/Base/BaseButton.vue"

export default {
  name: "Signup",
  components: {
    BaseInput,
    BaseButton
  },
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: ""
    }
  },
  computed: {
    validPassword() {
      return this.password === this.confirmPassword
    }
  }
}
</script>

<style>

</style>