<template>
  <div class="upload-container">
    <div class="upload-box">
      <input type="file" accept="image/*" ref="fileInput" style="display: none;" id="upload_img"
        @change="handleFileUpload">
      <div class="upload-button" @click="openFileUpload">
        <span v-if="!uploadedImageURL">点击上传图片</span>
        <img :src="uploadedImageURL" v-else>
      </div>
    </div>
    <div class="input-section">
      <div class="input-wrapper">
        <a-textarea v-model:value="textInput" show-count :maxlength="100" placeholder="请输入文字" />
      </div>
      <div class="button-wrapper">
        <a-button @click="SubmitImage" type="primary" shape="round" :size="size">提交图片-隐写</a-button>
      </div>
      <div class="button-wrapper">
        <a-button @click="DownloadImage" type="primary" shape="round" :size="size">
          <template #icon>
            <DownloadOutlined />
          </template>
          下载隐写后的图片
        </a-button>
      </div>
    </div>
  </div>
  <div v-if="showSteganImg">
    <img :src="steganImg" alt="steganImg" class="image" />
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent, ref, inject } from 'vue';
import { DownloadOutlined } from '@ant-design/icons-vue';
export default defineComponent({
  components: {
    DownloadOutlined,
  },
  setup() {
    const textInput = ref('');
    const url = inject('$url');
    return {
      textInput,
      size: ref('large'),
      url,
    };
  },
  data() {
    return {
      uploadedImageURL: null,
      uploadedImageFile: null,
      showSteganImg: false, // 控制是否显示隐写后的图片
      steganImg: '', // 隐写后的图片
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.uploadedImageURL = URL.createObjectURL(file);
        this.uploadedImageFile = file;
      }
    },
    openFileUpload() {
      this.$refs.fileInput.click();
    },
    SubmitImage() {
      // 上传图片及要隐写的文字
      // console.log(this.textInput)
      // console.log(this.uploadedImageFile)
      var text = this.textInput;
      if (text == '') {
        alert("请输入要隐写的文字！");
        return;
      }
      var file = this.uploadedImageFile;
      var formData = new FormData()
      console.log("uploadImage_stegan:")

      var jaccount = sessionStorage.getItem("jaccount");
      var that = this;

      formData.append("jaccount", jaccount);
      formData.append("upload_file", file);
      formData.append("text", text);

      axios
        .post(that.url + "/index/stegan/", formData)
        .then(function (response) {
          // 处理返回的图片格式并展示
          console.log(response.data["key"]);
          if (response.data["key"] == 1) {
            console.log("Stegan成功！");
            console.log(response.data['stegan_photo'])
            that.showSteganImg = true;
            that.steganImg = that.url + "/media/" + response.data['stegan_photo'];
          }
          if (response.data["key"] == 0) {
            console.log("Stegan失败！");
          }
        })
        .catch(function (error) {
          console.log(error)
        });

    },
    DownloadImage() {
      var stegan_photo = sessionStorage.getItem("stegan_photo");
      console.log("stegan_photo:");
      console.log(stegan_photo);
      // 拼接完整的图片URL
      var imageUrl = this.url + "/media/" + stegan_photo;

      // 发送GET请求获取图片数据
      axios.get(imageUrl, { responseType: 'blob' })
        .then(response => {
          // 创建一个下载链接
          var url = window.URL.createObjectURL(new Blob([response.data]));

          // 创建一个隐藏的下载链接，并模拟点击下载
          var link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', stegan_photo);
          link.style.display = 'none';
          document.body.appendChild(link);
          link.click();

          // 清理下载链接
          document.body.removeChild(link);
        })
        .catch(error => {
          console.error("下载图片失败:", error);
        });
    }
  }
});
</script>

<style>
.upload-container {
  display: flex;
  align-items: flex-start;
}

.upload-box {
  width: 400px;
  height: 400px;
  border: 2px dashed #aaa;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.upload-button {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.upload-button img {
  max-width: 100%;
  max-height: 100%;
}

.input-section {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
}

.input-wrapper {
  margin-bottom: 10px;
}

.button-wrapper {
  display: flex;
  justify-content: center;
  margin: 10px;
}
</style>
