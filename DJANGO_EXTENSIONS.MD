#ADD COOL FEATURES TO YOU DJANGO

https://github.com/django-extensions/django-extensions

install django-extensions
```commandline
pip install django-extensions
```

don't forget add to your settings.py
```python
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

## Creating models diagram
install library for drawing
```commandline
pip install pydotplus
```

```commandline
./manage.py graph_models -a -o myapp_models.png
```

my first example 
[myapp_models.png](myapp_models.png)

OTHER usefull commands
```commandline
python manage.py show_urls

python manage.py shell_plus
```

full docs 
https://django-extensions.readthedocs.io/en/latest/