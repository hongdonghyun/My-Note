#postgre 명령어
```
psql postgres
\password username
\q
```
```
user생성
createuser username
```

```
createdb --owner=username 만들db
```


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instragram',
        'USER': 'hdh',
        'PASSWORD': 'ghd43ehd1',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
```

```
pip install psycopg2
```