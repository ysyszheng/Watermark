<template>


  <div>
    <p :class="{ 'link': popupVisible1 }" @click="showPopup1">
      <a href="javascript:void(0)">登录</a>
    </p>
    <div v-if="popupVisible1" class="popup">
      <a href='http://localhost:8000/login/'>从jaccount登录</a>
      <button @click="hidePopup1">取消</button>
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

    showPopup1() {
      this.popupVisible1 = true
    },
    hidePopup1() {
      this.popupVisible1 = false
    },


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
