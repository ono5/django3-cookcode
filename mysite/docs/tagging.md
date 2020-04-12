# Tagging

You will do this by integrating a third-party Django tagging application into your project.

[django-taggit](https://github.com/jazzband/django-taggit)

```bash
pip install django_taggit==1.2.0
```

```bash
INSTLLED_APPS = [
    'taggit',
]
```

# How to use it?

```bash
python manage.py shell

>>> from blog.models import Post
>>> post = Post.objects.get(id=1)
>>> post.tags.add('music', 'jazz', 'django')
>>> post.tags.all()
<QuerySet [<Tag: music>, <Tag: django>, <Tag: jazz>]>
>>> post.tags.remove('django')
>>> post.tags.all()
<QuerySet [<Tag: music>, <Tag: jazz>]>
```

