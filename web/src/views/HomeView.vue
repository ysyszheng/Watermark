<template>
  <div v-if="!isLogged" class="jaccount" @click="login">
    <br />
    <p>通过jAccount登录</p>
    <img src="https://i.sjtu.edu.cn/css/assets/images/jaccount.png" alt="jAccount"/>
    <br />
  </div>
  <div v-else class="jaccount" @click="logout">
    <br />
    <p>从jAccount登出</p>
    <img src="https://i.sjtu.edu.cn/css/assets/images/jaccount.png" alt="jAccount"/>
    <br />
  </div>
</template>

<script>
import { ref, inject } from "vue";
export default {
  name: 'homepage',
  setup() {
    const isLogged = ref(false)
    const username = ref(null)
    const url = inject("$url");
    console.log("url: " + url)
    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) isLogged.value = false
    else {
      isLogged.value = true
      username.value = sessionStorage.getItem("name")
    }
    return{
      username,
      isLogged,
      url,
    }
  },
  methods:{
    login() {
      window.location.href = this.url + '/login/';
    },
    logout(){
      window.location.href = this.url + '/logout/';
    }
  },
}
</script>

<style>
.jaccount {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 320px;
  height: 112px;
  cursor: pointer;
}

.jaccount p {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  color: #c2c2c2;
}

.jaccount img {
  max-width: 100%;
  height: auto;
}

.jaccount:hover {
  background-color: #f6f6f6;
}
</style>

