#Documenting API with Swagger
[https://github.com/marcgibbons/django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger)
##Installation
### install package
`pip install django-rest-swagger`

###Add to INSTALLED_APPS
Add `rest_framework_swagger` to your `INSTALLED_APPS` setting:
```djangotemplate
INSTALLED_APPS = (
        ...
        'rest_framework_swagger',
    )
```
### add to urls.py
```djangotemplate
...
from rest_framework_swagger.views import get_swagger_view
...

schema_view = get_swagger_view(title='Pastebin API'),

urlpatterns = [
    ...
    url(r'^docs/swagger/', schema_view),
    ...
]
```

