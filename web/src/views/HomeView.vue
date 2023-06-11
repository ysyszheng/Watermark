<template>
  <div class="about">
    <h1>This is an home page.  </h1>
  </div>
  <div class="about">
    <h1>Hello {{username}}!</h1>
  </div>

  <div v-if="islogin">
    <p :class="{ 'link': popupVisible2 }" @click="showPopup2">
      <a href="javascript:void(0)">登出</a>
    </p>
    <div v-if="popupVisible2" class="popup">
      <p>确定需要登出吗？</p>
      <a href='http://localhost:8000/logout'>登出</a>
      <button @click="hidePopup2">关闭</button>
    </div>
  </div>


</template>

<script>
import { ref } from 'vue';
import axios from 'axios'
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
      islogin,

    }
  },

  watch: {
    username(to, from) {
      console.log("change:")
      console.log(to)
      location.reload()
    }
},

data() {
  return {
    popupVisible2: false,
  }
},

methods:{
    showPopup2() {
      this.popupVisible2 = true
    },

    hidePopup2() {
      this.popupVisible2 = false
    },




  LOGOUT(){


      // axios.post('http://localhost:8000/logout/',
      //     {
      //       request,
      //     })
      //   .then(response => {
      //     // 处理返回的数据
      //     console.log(response.data)
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
      // window.sessionStorage.clear();
      window.location.href = '/login';
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

.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border: 1px solid black;
}
</style>

