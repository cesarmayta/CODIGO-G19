1 - django-admin startproject blog
2 - cd blog
3 - python manage.py startapp web
4 - agregamos app al proyecto
    INSTALLED_APPS = [
    'web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

5 - configuramos base de datos mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

6- python manage.py migrate
