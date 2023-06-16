<template>
  <a-row>
    <a-col :span="8">
      <div v-if="isLogged" class="upload-box" @click="openFileUpload">
        <input type="file" accept="image/*" ref="fileInput" style="display: none;" id="upload_img"
          @change="handleFileUpload">
        <div class="upload-container">
          <span v-if="!uploadedImageURL">
            <div class="upload-text">
              点击上传图片, 仅支持png格式
            </div>
          </span>
          <img :src="uploadedImageURL" v-else>
        </div>
      </div>
    </a-col>
    <a-col :span="8">
      <div v-if="isLogged" class="input-button-container">
        <a-input v-model:value="textInput" placeholder="请输入版权证明文字" class="input-field" />
        <a-button @click="SubmitImage" type="primary" class="button">文字隐写</a-button>
        <a-button v-if="showSteganImg" @click="DownloadImage" type="primary" class="button">
          <template #icon>
            <DownloadOutlined />
          </template>
          下载隐写后的图片
        </a-button>
      </div>
    </a-col>
    <a-col :span="8">
      <div v-if="showSteganImg" class="stegan-container">
        <a-image :src="steganImg" alt="steganImg" />
      </div>
    </a-col>
  </a-row>
  <div v-if="!isLogged" class="jaccount" @click="mainpage">
    <br />
    <p>您尚未登录。请登录！</p>
    <img src="https://i.sjtu.edu.cn/css/assets/images/jaccount.png" alt="jAccount"/>
    <br />
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent, ref, inject } from 'vue';
import { notification } from 'ant-design-vue';
import { DownloadOutlined, InboxOutlined, PlusOutlined } from '@ant-design/icons-vue';

export default defineComponent({
  components: {
    DownloadOutlined,
    InboxOutlined,
    PlusOutlined,
  },
  setup() {
    const textInput = ref('');
    const url = inject('$url');
    const isLogged = ref(false);
    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) isLogged.value = false
    else {
      isLogged.value = true
    }
    return {
      textInput,
      size: ref('large'),
      url,
      isLogged,
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
    mainpage() {
      window.location.href = this.url + '/login/';
    },
    openFileUpload() {
      this.$refs.fileInput.click();
    },
    SubmitImage() {
      var text = this.textInput;
      var file = this.uploadedImageFile;
      if (file == null) {
        notification['error']({
          message: 'Error',
          description: '请上传图片！',
        });
        return;
      }
      if (text == '' || text == null) {
        notification['error']({
          message: 'Error',
          description: '请输入要隐写的版权文字！',
        });
        return;
      }
      if (!file.type.startsWith('image/png')) {
        notification['error']({
          message: 'Error',
          description: '图片格式不正确！',
        });
        return;
      }
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
            // that.steganImg = that.url + "/media/" + response.data['stegan_photo'];
            var imageData = response.data['stegan_photo'];
            const imageBytes = atob(imageData);

            // 创建一个 Uint8Array 来存储图片字节数据
            const imageArray = new Uint8Array(imageBytes.length);
            for (let i = 0; i < imageBytes.length; i++) {
              imageArray[i] = imageBytes.charCodeAt(i);
            }
            // 创建 Blob 对象并生成图片 URL
            const imageUrl = URL.createObjectURL(new Blob([imageArray], { type: 'image/jpeg' }));
            that.steganImg = imageUrl

            // sessionStorage.setItem("stegan_photo", response.data['stegan_photo']);
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
      // 创建一个隐藏的下载链接，并模拟点击下载
      var link = document.createElement('a');
      link.href = this.steganImg;
      // link.setAttribute('download', stegan_photo);
      link.setAttribute('download', 'stegan_photo.png');
      link.style.display = 'none';
      document.body.appendChild(link);
      link.click();

      // 清理下载链接
      document.body.removeChild(link);

    }
  }
});
</script>

<style>
.upload-box {
  width: 300px;
  height: 300px;
  border: 1.5px dashed #c2c2c2;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.upload-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.upload-container img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.upload-text {
  margin-top: 8px;
  color: #666;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.stegan-container {
  width: 300px;
  height: 300px;
  /* border: 2px solid #c2c2c2; */
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
}

.stegan-container a-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.input-container {
  display: flex;
  flex-direction: column;
  gap: 8px; /* 控制间距的属性 */
}

.input-field {
  margin-bottom: 8px; /* 添加下方间距 */
}

.button {
  margin-top: 8px; /* 添加上方间距 */
  margin-right: 20px; /* 添加右侧间距 */
}
</style>
