<template>
  <a-row>
    <a-col :span="8">
      <div class="upload-box" @click="openFileUpload">
        <input type="file" accept="image/*" ref="fileInput" style="display: none;" id="upload_img"
          @change="handleFileUpload">
        <div class="upload-container">
          <span v-if="!uploadedImageURL">
            <div class="upload-text">
              点击上传图片
            </div>
          </span>
          <img :src="uploadedImageURL" v-else>
        </div>
      </div>
    </a-col>
    <a-col :span="8">
      <div class="input-button-container">
        <a-input v-model:value="textInput" placeholder="请输入水印版权文字" class="input-field" />
        <a-button @click="SubmitImage" type="primary" class="button">添加水印</a-button>
        <a-button v-if="showWatermarkImg" @click="DownloadImage" type="primary" class="button">
          <template #icon>
            <DownloadOutlined />
          </template>
          下载添加水印后的图片
        </a-button>
      </div>
    </a-col>
    <a-col :span="8">
      <div v-if="showWatermarkImg" class="watermark-container">
        <a-image :src="watermarkImg" alt="watermarkImg" />
      </div>
    </a-col>
  </a-row>
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
      showWatermarkImg: false, // 控制是否显示隐写后的图片
      watermarkImg: '', // 隐写后的图片
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
          description: '请输入要添加的水印版权文字！',
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
      console.log("uploadImage_watermark:")

      var jaccount = sessionStorage.getItem("jaccount");
      var that = this;

      formData.append("jaccount", jaccount);
      formData.append("upload_file", file);
      formData.append("text", text);

      axios
        .post(that.url + "/index/watermark/", formData)
        .then(function (response) {
          // 处理返回的图片格式并展示
          console.log(response.data["key"]);
          if (response.data["key"] == 1) {
            console.log("Watermark成功！");
            console.log(response.data['watermark_photo'])
            that.showWatermarkImg = true;
            that.watermarkImg = that.url + "/media/" + response.data['watermark_photo'];
            sessionStorage.setItem("watermark_photo", response.data['watermark_photo']);
          }
          if (response.data["key"] == 0) {
            console.log("Watermark失败！");
          }
        })
        .catch(function (error) {
          console.log(error)
        });

    },
    DownloadImage() {
      var watermark_photo = sessionStorage.getItem("watermark_photo");
      console.log("watermark_photo:");
      console.log(watermark_photo);
      // 拼接完整的图片URL
      var imageUrl = this.url + "/media/" + watermark_photo;

      // 发送GET请求获取图片数据
      axios.get(imageUrl, { responseType: 'blob' })
        .then(response => {
          // 创建一个下载链接
          var url = window.URL.createObjectURL(new Blob([response.data]));

          // 创建一个隐藏的下载链接，并模拟点击下载
          var link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', watermark_photo);
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
  },
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

.watermark-container {
  width: 300px;
  height: 300px;
  /* border: 2px solid #c2c2c2; */
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
}

.watermark-container a-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.input-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  /* 控制间距的属性 */
}

.input-field {
  margin-bottom: 8px;
  /* 添加下方间距 */
}

.button {
  margin-top: 8px;
  /* 添加上方间距 */
  margin-right: 20px;
  /* 添加右侧间距 */
}</style>
