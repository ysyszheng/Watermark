<template>
  <div class="upload-container">
    <div class="upload-box">
      <input type="file" accept="image/*" ref="fileInput" style="display: none;" @change="handleFileUpload">
      <div class="upload-button" @click="openFileUpload">
        <span v-if="!uploadedImage">点击上传图片</span>
        <img :src="uploadedImage" v-else>
      </div>
    </div>
    <div class="input-section">
      <div class="input-wrapper">
        <input type="text" v-model="textInput" placeholder="请输入文字">
      </div>
      <div class="button-wrapper">
        <button @click="generateImage">生成带有文字的图片</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploadedImage: null,
      textInput: ''
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.uploadedImage = URL.createObjectURL(file);
      }
    },
    openFileUpload() {
      this.$refs.fileInput.click();
    },
    generateImage() {
      // 生成带有文字的图片的逻辑
    }
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
}
</style>
