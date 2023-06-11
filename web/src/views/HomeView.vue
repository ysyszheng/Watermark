<template>
  <div class="about">
    <h1>This is an home page.  </h1>
  </div>
  <div class="about">
    <h1>Hello {{username}}!</h1>
  </div>

<!--  <div v-if="islogin">-->
<!--    <p :class="{ 'link': popupVisible2 }" @click="showPopup2">-->
<!--      <a href="javascript:void(0)">登出</a>-->
<!--    </p>-->
<!--    <div v-if="popupVisible2" class="popup">-->
<!--      <p>确定需要登出吗？</p>-->
<!--      <button @click="LOGOUT">确定</button>-->
<!--      <button @click="hidePopup2">关闭</button>-->
<!--    </div>-->
<!--  </div>-->


</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

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
    timer: null, // 定时器
    intervalTime: 1000 * 60 * 10 // 定时器间隔时间，这里设置为10分钟
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
      window.location.href = 'http://localhost:8000/logout/';
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

