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
          label="Email"
          placeholder="email@bottlecaps.com"
          v-model:value="email"/>
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
          <BaseButton
            @click="signup"
            :disabled="invalidPassword || invalidUsername || invalidEmail">Create account</BaseButton>
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
      email: "",
      password: "",
      confirmPassword: ""
    }
  },
  computed: {
    invalidPassword() {
      return (this.password === "" || (this.password !== this.confirmPassword))
    },
    invalidUsername() {
      return this.username === ""
    },
    invalidEmail() {
      return this.email === ""
    }
  },
  methods: {
    async signup() {
      const data = await this.$store.dispatch('signup', {"username": this.username, "email": this.email, "password": this.password})
      if (!data.error) this.$router.push({name: 'home'})
    }
  }
}
</script>

<style>

</style>