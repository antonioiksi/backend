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


save png for all apps
```commandline
./manage.py graph_models -a -o myapp_models.png
```

save .dot for all apps
```commandline
./manage.py graph_models -a -o myapp_models.dot
```
for view and edit .dot files use 
[https://vincenthee.github.io/DotEditor/](https://vincenthee.github.io/DotEditor/)


for several apps
```commandline
./manage.py graph_models data_graph -o  data_graph.png
```

view and edit .dot files use opensource software
[https://vincenthee.github.io/DotEditor/](https://vincenthee.github.io/DotEditor/)


my first example 
[myapp_models.png](myapp_models.png)

OTHER usefull commands
```commandline
python manage.py show_urls

python manage.py shell_plus
```

full docs 
https://django-extensions.readthedocs.io/en/latest/