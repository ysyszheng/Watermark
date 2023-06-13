<template>
  <div class="bar">
    <nav class="navbar">
      <div class="nav-links">
        <RouterLink to="/" class="logo">数据隐写和隐私保护平台</RouterLink>
        <RouterLink to="/history" class="nav-link">历史记录</RouterLink>
        <RouterLink to="/steganography" class="nav-link">数据隐写</RouterLink>
        <RouterLink to="/watermark" class="nav-link">图片水印</RouterLink>
        <RouterLink to="/profile" class="nav-link">个人信息</RouterLink>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.bar {
  margin-bottom: 100px;
}
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f0f0f0;
}

.logo {
  font-weight: bold;
}

.nav-links {
  flex-grow: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-link {
  margin-right: 10px;
}

/* .nav-link:hover {
  background-color: #fff;
} */
</style>
