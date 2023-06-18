## 运行网页服务器的命令

1. 先删除本地db.sqlite3数据库
2. 启动Django（包括重建数据库）
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
3. 启动vue
    - npm run dev
