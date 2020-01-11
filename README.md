# Djangoの練習用リポジトリ

## Step1
### Setup

```bash
pip install django
```

### Project/Application作成

- プロジェクト作成

```bash
django-admin startproject {PJ_NAME}
```

- アプリケーションディレクトリ作成

```bash
cd {PJ_NAME} && python manage.py startapp {APP_NAME}
```

- 完成時のディレクトリ構成
```text
├── Makefile
├── django_app
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── memo_app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

### Update Files
#### Model
- models.py
- admin.py ※WebからDBをいじるために修正、そうでなければ不要
- `python manage.py createsuperuser` ※上記と同様

#### URL設定
- django_app/urls.py
- memo_app/urls.py (New)

#### Display設定
- memo_app/views.py
- templates/index.html (New)
