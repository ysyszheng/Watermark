<template>
  <div class="about">
    <h1>This is an home page.  </h1>
  </div>
  <div class="about">
    <h1>Hello {{username}}!</h1>
  </div>
</template>

<script>
import { ref } from 'vue';
export default {
  name: 'homepage',
  setup()
  {
    const islogin = ref(false)
    const username = ref(null)

    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) islogin.value = false
    else {
      islogin.value = true
      username.value = sessionStorage.getItem("name")
    }

    return{
      username,
      islogin
    }
  },

  watch: {
    username(to, from) {
      console.log("change:")
      console.log(to)
      location.reload()
    }
},


}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 20vh;
    display: flex;
    align-items: center;
  }
}
</style>

