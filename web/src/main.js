import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { Button, Input } from 'ant-design-vue';
// import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

const app = createApp(App)

app.provide('$url', 'http://localhost:8000')

app.use(router)
app.use(Button)
app.use(Input)

app.mount('#app')
