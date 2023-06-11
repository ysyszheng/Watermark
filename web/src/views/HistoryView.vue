<template>
  <div>
    <div v-for="image in imageSet" :key="image.id" class="image-item">
      <div class="image-info">
        <p>时间戳: {{ image.file_time }}</p>
        <p>文字信息: {{ image.text }}</p>
      </div>
      <div class="image-container">
        <div class="image-box">
          <img :src="getImageUrl(image.photo_clean)" alt="原图">
          <p>原图</p>
        </div>
        <div class="image-box">
          <img :src="getImageUrl(image.photo_processed)" alt="修改后的图">
          <p>修改后的图</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
      imageSet: [] // 存储历史图片记录
    }
  },
  mounted() {
    // 在页面加载时获取历史图片记录
    this.getHistoricalImages()
  },
  methods: {
    getHistoricalImages() {
      // 从sessionStorage中获取图片记录
      const imageSet = sessionStorage.getItem("image_set")
      if (imageSet) {
        this.imageSet = JSON.parse(imageSet)
      }
      console.log("imageSet: ")
      console.log(imageSet)
    },
    getImageUrl(filename) {
      // 生成图片的URL
      return this.url + "/media/" + filename
    }
  }
}
</script>

<style>
.image-item {
  margin-bottom: 20px;
}

.image-container {
  display: flex;
  align-items: center;
}

.image-box {
  margin-right: 20px;
}

.image-box img {
  max-width: 400px;
  max-height: 400px;
}
</style>
