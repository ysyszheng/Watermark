<template>
    <a-row>
        <a-col :span="8">
        <div class="upload-box" @click="openFileUpload">
            <input type="file" accept="image/*" ref="fileInput" style="display: none;" id="upload_img"
            @change="handleFileUpload">
            <div class="upload-container">
            <span v-if="!uploadedImageURL">
                <div class="upload-text">点击上传图片</div>
            </span>
            <img :src="uploadedImageURL" v-else>
            </div>
        </div>
        </a-col>
        <a-col :span="8">
            <a-button @click="SubmitProcessedImage" type="primary" style="margin-bottom: 8px;">提取隐藏版权文字内容</a-button>
            <a-typography-paragraph v-if="showUnsteganText">
                <div style="font-size: 18px;">版权文字信息: 
                    <a-typography-text strong>{{ unsteganText }}</a-typography-text>
                </div>
            </a-typography-paragraph>
        </a-col>
    </a-row>
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
            // textInput: '',
            showUnsteganText: false, // 控制是否显示反隐写文字内容
            unsteganText: '', // 反隐写的文字内容
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
                // console.log(this.uploadedImage)
            }
        },
        openFileUpload() {
            this.$refs.fileInput.click();
        },
        SubmitProcessedImage() {
            // 上传要反隐写的图片
            // console.log(this.textInput)
            // console.log(this.uploadedImageFile)
            var file = this.uploadedImageFile;
            var formData = new FormData()
            console.log("uploadImage_unstegan:")
            var jaccount = sessionStorage.getItem("jaccount");
            var that = this
            formData.append("jaccount", jaccount);
            formData.append("upload_file", file);

            axios
                .post(that.url + "/index/unstegan/", formData)
                .then(response => {
                    if (response.data["key"] == 1) {
                        console.log("Unstegan成功！");
                        console.log(response.data['unstegan_text']);
                        that.unsteganText = response.data['unstegan_text']; // 将反隐写的文字内容赋值给变量
                        that.showUnsteganText = true; // 反隐写成功后设置为true
                        sessionStorage.setItem("unstegan_text", response.data['unstegan_text']);
                    }
                    if (response.data["key"] == 0) {
                        console.log("Unstegan失败！");
                    }
                })
                .catch(error => {
                    console.log(error);
                });
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
</style>
