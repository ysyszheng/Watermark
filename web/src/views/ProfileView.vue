<template>



  <div>
    <p :class="{ 'link': popupVisible1 }" @click="showPopup1">
      <a href="javascript:void(0)">登出</a>
    </p>
    <div v-if="popupVisible1" class="popup">
      <p>确定需要登出吗？</p>

<!--      <a href='http://localhost:8000/login/'>从jaccount登录</a>-->
      <button @click="LOGOUT">确定</button>
      <button @click="hidePopup1">取消</button>
    </div>
  </div>

</template>

<script>
import {ref, onMounted, watch, inject } from "vue";
export default {
  setup() {
    const url = inject('$url');
    return{
      url
    }
  },
  data() {
    return {
      popupVisible2: false,
      popupVisible1: false
    }
  },
  methods: {
    /*login(){
      this.$root.$isLogged = true;
      this.isLogged = true;
      this.popupVisible1 = false
    },*/
    
    showPopup1() {
      this.popupVisible1 = true
    },
    hidePopup1() {
      this.popupVisible1 = false
    },
    LOGOUT(){
      window.location.href = this.url + '/logout/';
    }


  }
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
