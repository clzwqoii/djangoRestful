# djangoRestful

```
  1 安装pip   [https://pypi.python.org/pypi/pip#downloads]
       下载  pip-version.tar.gz    然后解压到一个目录
       安装python setup.py install
  2 安装django
       pip install django
       pip install django-filter
  3 安装djangorestframework  \
       pip install djangorestframework
  4 安装markdown
       pip install markdown
  5 创建一个项目
       python manage.py startproject HelloWorld     django-admin.py startproject HelloWorld
  6 创建项目app
       python manage.py startapp restApp
  7 安装mysql驱动
       pip install mysqlclient     然后在settings.py修改配置
  8 创建用户（后面权限管理会用到）
       python manage.py createsuperuser  (最好在cmd命令窗口使用, 最后放在最后一步做)
  9 数据库迁移同步
       1 python manage.py makemigrations
       2 python manage.py migrate
       3 使用前需要先注释一些引入和路由, 注释和models相关的引入
       权限[https://www.cnblogs.com/xiaojikuaipao/p/6009882.html]
           已有数据表或数据   生成models
           python 项目名称/manage.py inspectdb > 项目名称/模型APP名称/models.py
  10 启动
       python manage.py runserver 0.0.0.0:8000 [http://blog.csdn.net/svalbardksy/article/details/50548073]
  11 配置修改
       1 mysql配置
          'default': {
                # 'ENGINE': 'django.db.backends.sqlite3',
                # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'test',
                'USER': 'root',
                'PASSWORD': 'root',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            }
       2 djangorestframework配置     添加rest_framework和app(app的名称)
           INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'rest_framework',
                'app',
            ]
```
