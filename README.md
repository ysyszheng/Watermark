# 版权隐私保护平台

1. 安装依赖
    ```bash
    # web文件夹(Vue项目)
    npm install --save ant-design-vue
    npm install --save-dev babel-plugin-import
    ```
2. 运行项目
    ```bash
    # Django文件夹下
    python3 manage.py makemigrations
    # web文件夹下
    npm run dev
    ```
    - 注意，如果要运行该项目，需要配置以下几个地方
        - Django项目中的settings文件，里面的Secret_key替换成自己的Secret_key，还有Jaccount client ID和Key也替换成自己的。
        - Django/views.py文件夹中的RETURN_URL改成自己前端服务器的地址。
        - web/src/main.js中的url改成后端服务器的地址。
        - 由于我们项目运行的是https服务，因此还需要配置证书。
3. 文件代码结构
    ```
    Django/ 后端Django项目文件夹
        Django/  项目主文件夹
            log/  存放浏览器访问日志
            oauth.py  存放Jaccount第三方登录相关的内容
            views.py  实现登录、登出等相关逻辑
            ...
        index/   index项目文件夹
            process/  数据隐写、隐写提取、添加水印、去除水印的功能实现
            axios.py  接收前端发送的请求并且进行处理
            views.py  实现网页加载、返回历史记录等逻辑
            middleware.py  添加中间件，进行日志记录，日志存放在Django/log下
            ...
        media/  存放静态文件，具体上是每个用户上传的原图和隐写后的图以及加水印之后的图
        ssl/  存放https的自签名证书
        db.sqlite3  sqlite数据库文件
        manage.py  项目启动文件

    web/  前端Vue项目文件
        src/  项目源码文件夹
            ssl/  存放https的自签名证书
            api/  存放axios请求的配置文件
            router/  对前端页面实现路由，通过输入的不同路由，跳转到不同页面
            views/   不同的页面是由该文件夹下的若干.vue文件进行刻画的
                ...
            App.vue  主页面文件，调用router进行路由
            main.js  项目总配置文件，包含后端的地址
        vite.config.js  项目部署配置文件，包含Vue项目的https启动项，以及对外的端口
    ```