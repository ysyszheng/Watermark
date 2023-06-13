<template>
  <div>
    <a-alert message="左侧为原图, 右侧为添加版权隐写后的图片, 点击图片可以放大预览" type="info" />
    <div v-for="image in imageSet" :key="image.id">
      <div>
        <a-divider>{{ image.file_time }}</a-divider>
        <a-typography-paragraph>
          <blockquote style="font-size: 18px;">版权文字信息: 
            <a-typography-text strong>{{ image.text }}</a-typography-text>
          </blockquote>
        </a-typography-paragraph>
      </div>
      <a-row>
        <a-col :span="12">
          <div class="image-container">
            <a-image :src="getImageUrl(image.photo_clean)" alt="原图" />
          </div>
        </a-col>
        <a-col :span="12">
          <div class="image-container">
            <a-image :src="getImageUrl(image.photo_processed)" alt="修改后的图" />
          </div>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
import { inject } from "vue";
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
    console.log("mounted")
    var o = true
    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) {
      o = false
    }
    setTimeout((o) => {
      this.checkSessionStorage(o)
    }, 500, o)
  },
  methods: {
    getHistoricalImages() {
      // 从sessionStorage中获取图片记录
      const imageSet = sessionStorage.getItem("image_set")
      if (imageSet) {
        this.imageSet = JSON.parse(imageSet)
      }
      // console.log("imageSet: ")
      // console.log(imageSet)
    },
    getImageUrl(filename) {
      // 生成图片的URL
      var imageData = filename;
      console.log("imageData:")
      console.log(imageData)
      const imageBytes = atob(imageData);

      // 创建一个 Uint8Array 来存储图片字节数据
      const imageArray = new Uint8Array(imageBytes.length);
      for (let i = 0; i < imageBytes.length; i++) {
        imageArray[i] = imageBytes.charCodeAt(i);
      }
      // 创建 Blob 对象并生成图片 URL
      const imageUrl = URL.createObjectURL(new Blob([imageArray], { type: 'image/jpeg' }));
      console.log("OBJ URL:")
      console.log(imageUrl)
      return imageUrl
    }
  }
}
</script>

<style>
.image-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80%; /* 设置容器宽度为上级容器宽度的 80% */
  max-width: 100%; /* 限制容器最大宽度为上级容器宽度的 80% */
}

.image-container a-image {
  width: 100%; /* 设置图片宽度为容器宽度的 100% */
  height: auto; /* 自动计算图片高度，保持宽高比 */
  object-fit: contain; /* 控制图片按比例缩放并完整显示在容器内 */
}
</style>
