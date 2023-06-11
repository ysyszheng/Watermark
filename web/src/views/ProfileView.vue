<template>


  <div>
    <p :class="{ 'link': popupVisible1 }" @click="showPopup1">
      <a href="javascript:void(0)">登录</a>
    </p>
    <div v-if="popupVisible1" class="popup">
      <a href='http://localhost:8000/login'>从jaccount登录</a>
      <button @click="hidePopup1">取消</button>
    </div>
  </div>

  <div v-if="isLogin === true">
    <p :class="{ 'link': popupVisible2 }" @click="showPopup2">
      <a href="javascript:void(0)">登出</a>
    </p>
    <div v-if="popupVisible2" class="popup">
      <p>确定需要登出吗？</p>
<!--      <button @click="LOGOUT">确认</button>-->
      <button @click="hidePopup2">关闭</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLogin:false,
      popupVisible1: false,
      popupVisible2: false,
      user: {
        id: '',
        name: ''
      }
    }
  },
  methods: {
    showPopup1() {
      this.popupVisible1 = true
    },
      showPopup2() {
        this.popupVisible2 = true
      },
      hidePopup1() {
        this.popupVisible1 = false
      },
      hidePopup2() {
        this.popupVisible2 = false
      },
    mounted() {
      axios.get('/api/user').then(response => {this.user = response.data})
    },
    LOGOUT(){
      /*axios.post('/api/logout').then(response => {
      // 清除用户信息
      this.user = {
        id: '',
        name: ''
          }
      })*/

      this.isLogged = true;
      window.location.href = '/login';
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
