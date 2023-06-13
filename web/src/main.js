// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {
  Button, Input, Layout, Menu, 
  Breadcrumb, Divider, Image, Grid, 
  Row, Col, Typography, Upload,
  Alert,
} from 'ant-design-vue';
// import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

const app = createApp(App)

app.provide('$url', 'https://10.119.11.199:443')
app.use(router)
app.use(Button)
app.use(Input)
app.use(Layout)
app.use(Menu)
app.use(Breadcrumb)
app.use(Divider)
app.use(Image)
app.use(Grid)
app.use(Row)
app.use(Col)
app.use(Typography)
app.use(Upload)
app.use(Alert)

app.mount('#app')
