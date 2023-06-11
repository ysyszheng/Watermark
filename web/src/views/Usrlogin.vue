<template>
  <div>
    <p :class="{ 'link': popupVisible1 }" @click="showPopup1">
      <a href="javascript:void(0)">登录</a>
    </p>
    <div v-if="popupVisible1" class="popup">
      <button @click="LOGIN">通过jaccount登录</button>
      <button @click="hidePopup1">取消</button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch, inject } from "vue";
export default {
  setup() {
    const url = inject('$url');
    return {
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
    showPopup1() {
      this.popupVisible1 = true
    },
    hidePopup1() {
      this.popupVisible1 = false
    },
    LOGIN() {
      window.location.href = this.url + '/login/';
    }
  }
}
</script>

<style>
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
