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
            <div class="button-wrapper">
                <a-button @click="SubmitProcessedImage" type="primary" shape="round" :size="size">提取隐写内容</a-button>
                <div v-if="showUnsteganText">{{ unsteganText }}</div>
            </div>
        </div>
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

.button-wrapper {
    display: flex;
    justify-content: center;
    margin: 10px;
}
</style>
