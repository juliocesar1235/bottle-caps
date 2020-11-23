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
      <div class="flex items-center justify-between">
        <BaseButton>Login</BaseButton>
        <router-link :to="{name: 'signup'}">
          <BaseButton :flat="true">Create account</BaseButton>
        </router-link>
      </div>
    </form>
  </div>
</template>

<script>
import BaseInput from "@/components/Base/BaseInput.vue"
import BaseButton from "@/components/Base/BaseButton.vue"

export default {
  name: "Login",
  components: {
    BaseInput,
    BaseButton
  },
  data() {
    return {
      username: "",
      password: ""
    }
  }
};
</script>
