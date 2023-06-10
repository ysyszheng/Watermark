<template>


  <div>
    <p :class="{ 'link': popupVisible1 }" @click="showPopup1">
      <a href="javascript:void(0)">登录</a>
    </p>
    <div v-if="popupVisible1" class="popup">
      <a href='http://localhost:5173/history'>从jaccount登录</a>
      <button @click="hidePopup1">取消</button>
    </div>
  </div>

  <div>
    <p :class="{ 'link': popupVisible2 }" @click="showPopup2">
      <a href="javascript:void(0)">登出</a>
    </p>
    <div v-if="popupVisible2" class="popup">
      <p>确定需要登出吗？</p>
      <button @click="LOGOUT">确认</button>
      <button @click="hidePopup2">关闭</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      popupVisible2: false,
      popupVisible1: false
    }
  },
  methods: {
    showPopup2() {
      this.popupVisible2 = true
    },
    showPopup1() {
      this.popupVisible1 = true
    },
    hidePopup1() {
      this.popupVisible1 = false
    },
    hidePopup2() {
      this.popupVisible2 = false
    },
    LOGOUT(){
      // 执行注销操作
      // 例如：发送请求到后端，清除用户信息等
      // 然后跳转到登录页面
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
