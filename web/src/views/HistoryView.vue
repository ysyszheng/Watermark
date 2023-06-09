<template>
  <div>
    <img :src="imageUrl1" alt="test.png" class="image"/>
    <h1>{{ fileName1 }}</h1>
    <h1>时间：{{ formattedTime }}</h1>
    <img :src="imageUrl2" alt="lucky.png" class="image"/>
    <h1>时间：{{ formattedTime }}</h1>
  </div>
</template>



<script>
export default {
  /*data() {
    return {
      imageUrl1: 'src/picture/test.png' ,// 图片的本地地址
      imageUrl2: 'src/picture/20230609215900.png'
    }
  },*/
  data() {
    return {
      imageUrl2: 'src/picture/20230609220001.png',// 图片的本地地址
      imageUrl1: 'src/picture/20230609215900.png',
      fileName1: '20230609215900.png'
    }
  },
  computed: {
    formattedTime() {
      // 将14位数字转换为时间格式
      const year = this.fileName1.substring(0, 4)
      const month = this.fileName1.substring(4, 6)
      const day = this.fileName1.substring(6, 8)
      const hour = this.fileName1.substring(8, 10)
      const minute = this.fileName1.substring(10, 12)
      const second = this.fileName1.substring(12, 14)
      const time = `${year}.${month}.${day} ${hour}:${minute}:${second}`
      return time
    }
  }
}
</script>



<style>
.image {
  max-width: 100%;
  max-height: 200px;
  margin-bottom: 10px;
}
</style>