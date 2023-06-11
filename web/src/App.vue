<!-- <script setup>
import Header from './components/Header.vue';
</script> -->

<template>
  <div class="bar">
    <nav class="navbar">
      <div class="nav-links">
        <RouterLink to="/" class="logo">数据隐写和隐私保护平台</RouterLink>
        <RouterLink v-if="isLogged" to="/history" class="nav-link">历史记录</RouterLink>
        <RouterLink v-if="isLogged" to="/steganography" class="nav-link">数据隐写</RouterLink>
        <RouterLink v-if="isLogged" to="/watermark" class="nav-link">图片水印</RouterLink>
        <RouterLink v-if="!isLogged" to="/login" class="nav-link">账号登录</RouterLink>
<!--        <RouterLink v-if="isLogged" to="/profile" class="nav-link">账号登出</RouterLink>-->
      </div>
    </nav>
  </div>

  <RouterView />
</template>

<script>
// import { getid } from "./api/api.js";
import {ref, onMounted, watch } from "vue";
import axios from "axios";
import axiosInstance from './api/index.js'
import {getid} from "@/api/api";
export default {
  name: "App",
  setup() {
    const axios = axiosInstance
    const getid = () => {
      return axios.get('http://localhost:8000')
    }

    console.log("reload");

    // const response = getid();

    axios
        .get('http://localhost:8000')
        .then((response) => {
          console.log("Hello ")
          console.log(response.data["name"])
          console.log(response.data["image_set"])

          sessionStorage.setItem("name", response.data["name"]);
          sessionStorage.setItem("jaccount", response.data["account"]);

        })
    const isLogged = ref(false)
    const username = ref(null)

    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) isLogged.value = false
    else {
      isLogged.value = true
      username.value = sessionStorage.getItem("name")
    }


        // sessionStorage.setItem("name", response.data["name"]);
        // sessionStorage.setItem("jaccount", response.data["account"]);
        //
        // const jsonStr = JSON.stringify(response.data["image_set"]);
        // sessionStorage.setItem("image_set", jsonStr);
      return {
      getid,
      username,
      isLogged,

    }




        },


    // onMounted(() => {
    //   getid();
    // });










  // data() {
  //   return {
  //     isLogged: true
  //   }
  // }


}






</script>

<style scoped>
.bar {
  margin-bottom: 100px;
}
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f0f0f0;
}

.logo {
  font-weight: bold;
}

.nav-links {
  flex-grow: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-link {
  margin-right: 10px;
}

/* .nav-link:hover {
  background-color: #fff;
} */
</style>
