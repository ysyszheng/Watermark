<template>
  <a-layout style="min-height: 100vh">
    <!-- <a-layout-sider v-model:collapsed="collapsed" collapsible> -->
    <a-layout-sider>
      <div class="logo">
        <span>版权隐私保护平台</span>
      </div>
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item key="1" v-if="isLogged">
          <history-outlined />
          <span></span><RouterLink to="/history">历史记录</RouterLink>
        </a-menu-item>
        <a-sub-menu key="sub1" v-if="isLogged">
          <template #title>
            <span>
              <file-protect-outlined />
              <span></span><RouterLink to="/steganography">数据隐写</RouterLink>
            </span>
          </template>
          <a-menu-item key="2">图片隐写</a-menu-item>
          <a-menu-item key="3">隐写提取</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2" v-if="isLogged">
          <template #title>
            <span>
              <file-image-outlined />
              <span></span><RouterLink to="/watermark">图片水印</RouterLink>
            </span>
          </template>
          <a-menu-item key="4">添加水印</a-menu-item>
          <a-menu-item key="5">去除水印</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="6">
          <user-outlined />
          <span></span><RouterLink to="/login">账号登录</RouterLink>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0" />
      <a-layout-content style="margin: 0 16px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>Hello</a-breadcrumb-item>
          <a-breadcrumb-item v-if="isLogged">{{ username }}</a-breadcrumb-item>
        </a-breadcrumb>
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
          <RouterView />
        </div>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
        版权隐私保护平台 ©2023 Created by 应用软件安全 Group 4
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script>
import {
  PieChartOutlined,
  DesktopOutlined,
  UserOutlined,
  HistoryOutlined,
  FileImageOutlined,
  FileProtectOutlined,
} from '@ant-design/icons-vue';
import { defineComponent, ref, onMounted } from 'vue';
import axiosInstance from './api/index.js'

export default defineComponent ({
  name: "App",
  components: {
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    HistoryOutlined,
    FileImageOutlined,
    FileProtectOutlined,
  },
  setup() {
    const axios = axiosInstance
    const getid = () => {
      return axios.get('http://localhost:8000')
    }

    console.log("reload");

    axios
      .get('http://localhost:8000')
      .then((response) => {
        console.log("Hello ")
        console.log(response.data["name"])
        console.log(response.data["image_set"])

        sessionStorage.setItem("name", response.data["name"]);
        sessionStorage.setItem("jaccount", response.data["account"]);
        const jsonStr = JSON.stringify(response.data["image_set"]);
        sessionStorage.setItem("image_set", jsonStr);

      })

    const isLogged = ref(false)
    const username = ref(null)

    if (sessionStorage.getItem("jaccount") == "0000" | sessionStorage.getItem("jaccount") == null) isLogged.value = false
    else {
      isLogged.value = true
      username.value = sessionStorage.getItem("name")
    }

    return {
      getid,
      username,
      isLogged,
      collapsed: ref(false),
      selectedKeys: ref(['1']),
    }

    onMounted(() => {
      getid();
    });
  },
})

</script>

<style>
.logo {
  height: 32px;
  margin: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 18px;
}

.site-layout .site-layout-background {
  background: #fff;
}
[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}
</style>