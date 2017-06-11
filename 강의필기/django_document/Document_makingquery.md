[원본](https://docs.djangoproject.com/en/1.11/topics/db/queries/)

# makemigrations
```

./manage.py migrate 앱폴더 이름 되돌리고 싶은 migrations이름명

./manage.py showmigrations  

확인 후 지울거 지움
```

```
같은 이름의 db를 가지려할때 migrate에서 에러가 남
이때 fake옵션을 주어서 강제함
./manage.py migrate --fake
```
# Making queries

설명의 기본이 되는 소스

```
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
```

```
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
```
SQL문의 INSERT에 해당하는 동작

save()를 하기전 까지는 데이터베이스에 접근하지 않는다.

# Saving changes to objects

```
>>> b5.name = 'New name'
>>> b5.save()
```
이미 데이터가 있는경우 위와 같은 동작을 하게 되면 SQL문의 UPDATE와 같은 동작을 한다.

# Saving ForeignKey and ManyToManyField fields

MTM필드에서 정보를 업데이트를 하려는 경우 add메서드를 사용하여 정보를 추가하여 업데이트를 한다.

```
from 추가할 모델 import 클래스
joe =Author.objects.create(name ="joe")
entry.authors.add(joe)
```
여러개의 값을 동시에 추가하려면
```
entry.authors.add(x1,x2,x3...)
```

# Retrieving objects

DB에서 객체를 검색하려면 모델 클래스의 manager를 통하여 Queryset을 생성해야한다.
```
b = Blog(name='Foo',tagline='Bar')
```

ex) `Blog.objects.all()`은 DB의 모든 Blog객체를 포함하는 Queryset을 반환

# Retrieving all objcets

데이터 테이블에서 개체를 검색하는 가장 간단한 방법은 all메서드를 사용하는것이다.
```
all_entries = Entry.objcets.all()
```

# Retrieving specific objects whti filters
all 메서드가 모든 객체를 반환하는 Queryset을 보여준다면 일부만 보기위해선 다음과 같은 메서드들을 사용해야한다.

- filter(**kwargs)
	- 지정된 매개변수와 일치하는 객체가 포함된 Queryset을 반환.
- exclude(**kwargs)
	- 지정된 매개변수와 일치하지 않는 객체를 Queryset으로 반환.

**kwargs의 형식은 다음과 같은 방식들이다.

- `Entry.objects.filter(pub_date__year=2006)`
- `Entry.objects.all().filter(pub_date__year=2006)`

>위와 아래의 형식은 같은값을 출력한다.

# Chaining filters
`filter`로 나온 결과는 쿼Queryset리셋 자체이므로 다시 필터를 적용시킬 수 있다.

```
Entry.objects.filter(
headline__startswith='what')
.exclude(
pub_date__gte=datetime.date.today())
.filter(
pub_date__gte=datetime(2005,1,30))
```
>startswith=???은 ???으로 시작하는 문자열을 찾는 조건
>gte 는 greater the equal 크거나 같은조건

# Filtered QUerySets are unique
Queryset을 필터할때마다 이전 Queryset에 필터링된 새로운 Queryset을 얻게된다.
필터링을 할때마다 재사용이 가능한 새로운 Queryset을 생성한다.

```
q1 =
Entry.objects.filter(headline__startswith="what")
q2 =
q1.exclude(pub_date__gte=datetime.date.today())
q3 = 
q1.filter(pub_date__gte=datetime.date.today())
```
>위와 같은 예제를 실행해도 실제 DB에는 반영되지 않는다.

# Retrieving a single object with get()
filter는 단일객체만 일치하는경우에도 항상 Queryset을 반환한다. (단일요소만 들어있는 Queryset)

쿼리와 일치하는 객체가 하나뿐인경우(만든요소가 하나뿐일때라던가)객체를 직접 반환하는 Manager에서 get()메서드를 사용할 수 있다.

`
one_entry = Entry.objects.get(pk=1)
`
>get은 filter와 마찬가지로 모든 쿼리표현식을 사용할 수있다.
>get() 값을 안주고 사용한다면 가지고올때 값이 하나뿐이라면 가져오지만 두개이상 존재하면 에러가 발생한다.

# Other Queryset methods

[Queryset API](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#queryset-api)

# Limiting Querysets
python의 슬라이스문을 메서드 뒤에 사용가능하다.
```
Entry.objects.all()[:5]
Entry.objects.all()[5:10]
```
>[start:stop:step]	
>단[-1]같은 음수연산은 불가하다.

목록이 아닌 단일객체를 반환하려면
`Entry.objects.order_by('headline')[0]`와 같이 사용하면 된다.

# Field lookups

[field lookup reference]
(https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups)

- exact : 똑같은값 찾기
`Entry.objects.get(headline__exact='Cat bites dog')` 




`Blog objects.get(id__exact=14)`
`Blog.objects.get(id=14)`

>위와 아래의 코드는 똑같은 결과를 반환한다.

- iexact : 대소문자를 구분하지않는 똑같은값 찾기
` Blog.objects.get(name__iexact='beatles blog')`

- contains : 대소문자를 구분하며 문자를 포함하는쿼리를 찾기
`Entry.objects.get(headline__contains='Lennon'`

- icontains : 대소문자를 구분하지 않고 문자를 포함하는 쿼리를 찾기
`Entry.objects.get(headline__icontains='Lennon'`

- startswith , endswith : 시작하는문자, 끝나는 문자 찾기
>istartswith, iendswith는 대소문자를 구분하지 않는다.

# Lookups that span relationships

필터 조건문에 __(더블언더스코어)를 사용하면 조건을 걸 수 있다.
`Blog.objects.filter(entry__authors__name__isnull = True`
isnull은 값이 null일경우 True반환
>조건사이에 ,를 찍으면 and연산

`Blog.objects.filter(entry__headline__contains="Lennon',entry__pub_date__year=2008)
`
`Blog.objects.filter(entry__headline__contains="Lennon").filter(entry__pub_date__year=2008)`
>위의 코드는 , 를 사용했고 Lennon이 포함되면서 2008년에 나온 항목을 모두 찾는다.
>아래의 코드는 .filter를 사용했고 Lennon이 포함되었거나 2008년에 나온 항목을 모두 찾는다.
>굳이 따지자면 ,는 and고 .filter는 or다

## exclude에서 필터 사용시

```
Blog.objects.exclude(
entry__headline__contains="Lennon",
entry__pub_date__year=2008,
)
```
>헤드라인에 Lennon이 들어있는 블로그와 2008년에 나온 블로그를 모두 제외 시킨다.


```
Blog.objects.exclude(
entry__in=Entry.objects.filter(
headline__contains ="Lennon",
pub_date__year=2008,
),
)
```
>헤드라인에 Lennon이 들어가있고 2008년에 나온 블로그만 제외 시킨다.

## Filters can reference fields on the model

모델 필드들의 값을 비교하게 해주는 F모델이 있다.
```
from django.db.models import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
```
>Django에서는 +,-,*,/,%등의 연산이 가능하다.

날짜/시간 필드의 경우 timedelta를 사용하여 더하거나 뺄 수 있다.

```
from datetime import timedelta
Entry.objects.filter(mod_date__gt=F('pub_date')+timedelta(days=3))
```

F모듈은 `.bitand()`, `.bitor()`, `.bitrightshift()`, `.bitleftshift()` 연산이 가능하다.

## complex lookups with Q objects
쿼리안에서 AND나 OR등의 조건을 걸 수 있게 해주는 모델

```
from django.db.models import Q
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```


