## 后端提供的数据接口
- 前端上传图片和文字，点击“提交图片-隐写”，后端会对发送的图片及文本进行隐写，并且返回前端一个文件名；前端可以通过该文件名(filename)，直接访问“127.0.0.1:8000/media/filename”来获取当前返回的隐写图片。数据库存储的内容是：原图文件名、时间戳、文本、隐写后图的文件名。
    - 需要做的是将本图片显示在当前页面右侧
    - 返回的图片位于`SteganographyView.vue`的SubmitImage()函数中，`response.data['stegan_photo']`变量中
- 前端上传已隐写图片，点击“提交图片-反隐写”，后端会处理图片，并且返回一个字符串，该字符串就是隐写的信息。数据库存储的内容是：上传的隐写图文件名、时间戳、文本。
    - 需要做的是将提取的信息显示在页面上
    - 返回的信息位于`SteganographyView.vue`的SubmitProcessedImage()函数中，`response.data['unstegan_text']`变量中

- 前端进行刷新的时候，前端会收到后端发来的JSON格式的数据，其中所有的历史记录存在`App.vue`文件的`response.data["image_set"]`中，需要显示在历史记录页面。需要注意的是，我返回的内容仅仅包括点击“隐写”按钮生成的数据，包括原图文件名、时间戳、文本、隐写后图的文件名，而不包括“反隐写”按钮生成的数据。


## 运行网页服务器的命令

1. 先删除本地db.sqlite3数据库
2. 启动Django（包括重建数据库）
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
3. 启动vue
    - npm run dev
