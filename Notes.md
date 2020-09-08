# Notes

## Ch2

- `settings.py` file controls the project settings
- `urls.py` tell django which pages to build in resonse to a browser or url request
- `wsgi.py` stands for WEB SERVER GATEWAY INTERFACE and helps django serce our eventual web pages
- `manage.py` is used to execute various django commands such as running the web server or creating a new app

> _To create a new project:_ `django-admin startproject {project_name} .` > _To create a new app:_ `python manage.py startapp {app_name}`

• `admin.py` is a configuration file for the built-in Django Admin app

• `apps.py` is a configuration file for the app itself

• `migrations/` keeps track of any changes to our models.py file so our database and models\.py stay in sync

• `models.py` iswherewedefineourdatabasemodels,whichDjangoautomatically translates into database tables

• `tests.py` is for our app-specific tests

In Django, _Views_ determine what content is displayed on a given page while _URLConfs_ determine where that content is going.

Our urlpattern has three parts:
• a Python regular expression
• specify the view
• add an optional url name

## Ch3

### **Templates**

To generate HTML files, in django, the approach is to use templates so that individual HTML files can be served by a view to a web page specified by the URL.

> Note: `Templates -> Views -> URLs`

The order in which you create them doesn't matter since all three are needed to work together. The URLs control the initial route which is the entry point into a page, the vies contain the logic and the template has the HTML. For websites that rely on the database model it is the view that determines what data is available to the template.

### Class-based views

The Buit-in `TemplateBView` to display our template.

### URLs

The last step is to update our URLConfs. This update needs to be made in two locations: first we update the project-level `urls.py` file to point to the `pages` app, then within `pages` we match the views to routes.
