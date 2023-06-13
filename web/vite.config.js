import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const fs = require('fs')
const path = require('path')

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    port: 443,
    // 是否开启 https
    https: {
      cert: fs.readFileSync(path.join(__dirname, 'src/ssl/cert.crt')),
      key: fs.readFileSync(path.join(__dirname, 'src/ssl/cert.key')),
    },
  },
})
