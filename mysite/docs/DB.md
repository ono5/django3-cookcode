# DB

## Check SQL

```bash
$ python manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(10) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

## postgres in docker

```bash
docker run --name postgres-local -p 5433:5432 -v ~/.postgres-data:/var/lib/postgresql/data  -e POSTGRES_PASSWORD=postgres -d postgres:10.8

docker container start
```

## Search

```bash

INSTALLED_APPS = [
    'django.contrib.postgres',
]
```

```bash
from blog.models import Post

Post.objects.filter(body__search='django')S
```

Multiple fields

```bash
from django.contrib.postgres.search import SearchVector
from blog.models import Post

Post.objects.annotate(
    search=SearchVector('title', 'body'),
).filter(search='django')
```