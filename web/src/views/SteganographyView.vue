<template>
  <div class="upload-container">
    <div class="upload-box">
      <input type="file" accept="image/*" ref="fileInput" style="display: none;" id="upload_img" @change="handleFileUpload">
      <div class="upload-button" @click="openFileUpload">
        <span v-if="!uploadedImageURL">点击上传图片</span>
        <img :src="uploadedImageURL" v-else>
      </div>
    </div>
    <div class="input-section">
      <div class="input-wrapper">
        <input type="text" v-model="textInput" placeholder="请输入文字">
      </div>
      <div class="button-wrapper">
        <button @click="generateImage">生成带有文字的图片</button>
      </div>
      <div class="button-wrapper">
        <button @click="SubmitImage">提交图片</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      uploadedImageURL: null,
      uploadedImageFile: null,
      textInput: ''
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.uploadedImageURL = URL.createObjectURL(file);
        this.uploadedImageFile = file;
        // console.log(this.uploadedImage)
      }
    },
    openFileUpload() {
      this.$refs.fileInput.click();
    },
    generateImage() {
      // 生成带有文字的图片的逻辑
    },
    SubmitImage() {
      // 上传图片及要隐写的文字
      // console.log(this.textInput)
      // console.log(this.uploadedImageFile)

      var text = this.textInput;
      var file = this.uploadedImageFile;
      var formData = new FormData()
      console.log("uploadImage_stegan:")

      var jaccount = sessionStorage.getItem("jaccount");

      formData.append("jaccount", jaccount);
      formData.append("upload_file", file);
      formData.append("text", text);

      axios
        .post("http://localhost:8000/index/stegan/", formData)
        .then(function (response)
        {
          // 处理返回的图片格式并展示
            console.log(response.data["key"]);
            if (response.data["key"] == 1) {
              console.log("Stegan成功！");
            }
            if (response.data["key"] == 0) {
              console.log("Stegan失败！");
            }
        })
        .catch(function (error){
          console.log(error)
        });

    },
  }
};
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
