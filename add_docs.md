#Documenting API

##Installation
### install package
`pip install coreapi`


### add to urls.py
```python
from rest_framework.documentation import include_docs_urls
...
urlpatterns = [
    ...
    url(r'^docs/', include_docs_urls(title='My API title')),
    ...
]
```

### include 2 views

- `/docs/`
- `/docs/schema.js`