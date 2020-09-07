## Ch2

- `settings.py` file controls the project settings
- `urls.py` tell django which pages to build in resonse to a browser or url request
- `wsgi.py` stands for WEB SERVER GATEWAY INTERFACE  and helps django serce our eventual web pages
- `manage.py` is used to execute various django commands such as running the web server or creating a new app

> *To create a new project:* `django-admin startproject {project_name} .`

> *To create a new app:* `python manage.py startapp {app_name}`

• `admin.py` is a configuration file for the built-in Django Admin app 

• `apps.py` is a configuration file for the app itself 

• `migrations/` keeps track of any changes to our models.py file so our database and models\.py stay in sync 

• `models.py` iswherewedefineourdatabasemodels,whichDjangoautomatically translates into database tables 

• `tests.py` is for our app-specific tests

In Django, *Views* determine what content is displayed on a given page while *URLConfs* determine where that content is going.


Our urlpattern has three parts:
• a Python regular expression
• specify the view 
• add an optional url name