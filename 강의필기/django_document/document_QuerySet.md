[원본](https://docs.djangoproject.com/en/1.11/ref/models/querysets/)

# QuerySet API reference

QuerySet은 DB에 저장되지 않고 먼저 체크 가능하다.

QuerySet의 모든항목을 print하고 싶을때

```
for e ind Entry.objects.all():
	print(e.headline)
```


## Pickling QueySets
??? 어케하는거냐

>QuerySet pickle은 사용된 Django버전에서만 유효하다
>다른버전에서는 안되므로 유의해야함.


## annotate()
```
annotate(*args,**kwargs)
```
반환되는 QuerySet의 객체에 추가되는 주석

```
from django.db.models import Count
q = Blog.objects.annotate(Count('entry'))

q[0].name
#무언가가 나옴
q[0].entry__count
#entry에서 카운트한숫자가 나옴

```

##order_by()
order_by(*fields)

QuerySet의 반환 결과는 정렬옵션에 주어진 순서에 의해서 정렬 된다.

```
Entry.objects.filter(pub_date__year=2005)
.order_by('-pub_date','headline')

```
>위 코드의 결과는
pub_date기준으로 내림차순으로 정렬 된 뒤 headline을 기준으로 오름차순으로 정렬 된다.
'-'는 내림차순을 나타낸다.
무작위로 하고 싶다면 '?'를 사용한다.(느릴수도있다)

또한 쿼리표현식에서 asc(),desc()를 사용하여 정렬을 할수도 있다.

```
Entry.objects.order_by('blog').desc()
```
> order_by(Lower('headline').desc())
> 를 사용하면 소문자로 변환하여 정렬

order_by호출을 여러번 사용 할 경우
제일 뒤에 있는 order_by가 적용된다.

## reverse()
쿼리셋이 반환되는 순서를 바꾼다.

```
my_queryset.reverse()[:5]
```
마지막 5개의 쿼리셋을 반환한다.
>reverse()를 쓰려면 order_by로 정렬되어 있는 쿼리셋에서만 가능하다.
>정렬이 되어있지않다면 효과가 없다고 한다.

## distinct()
`distinct(*fields)`

중복된 값을 제거한 후 쿼리셋을 반환한다.
>쿼리셋은 기본적으로 중복값을 제외하지 않는다.

## values()
`values(*fields,**expressions)`
반환값이 딕셔너리이다.

```
Blog.objects.filter(name__startswith='Beatles')
# <QuerySet [<Blog: Beatles Blog>]>

Blog.objects.filter(name__startswith='Beatles').values()
# <QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
```

## values_list()
`values_list(*fields,flat=False)`
values()와 사용법이 비슷하다.
차이점은 반환값이 딕셔너리가 아니라 튜플이라는 점이다.
>flat =True면 반환결과가 단일 튜플이 아닌 단일 값임

## dates()

```
dates(field,kind,order='ASC')

Entry.objects.dates('pub_date','year',order='DESC')
```

## none()
none()을 호출하면 객체를 반환하지 않는 쿼리셋이 만들어 진다.

`Entry.objects.none()
`
## union()
두개이상의 쿼리셋 결과를 합친다.

`qs1.union(qs2,qs3)
`

## intersection()
`
qs1.intersection(qs2,qs3)
`
쿼리셋의 교집합을 반환

## difference()
`
qs1.difference(qs2,qs3)
`
쿼리셋의 차집함을 반환

## defer()
`
Entry.objects.defer('headline','body')
`
제외검색

## only()

`
Person.objects.only('name')
`
유일검색

## using()
`
Entry.objects.using('backup')
`
DB 별칭지정

## get_or_create()

`
get_or_create(defaults=None,**kwargs)
`
찾거나 없을경우 만드는 메서드

```
obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
```
obj에 만들어진 걸 반환하고 Created에 bool대수를 반환
True이면 만들어진거고 False면 이미 있다는것

## update_or_create()

업데이트 하거나 없을경우 만드는 메서드
사용법은 get_or_create()와 같다.

## bulk_create()
`
bulk_create(objs,batch_size=None)
`
DB에 추가하는것


## in_bulk()
기본 키 값을 가져와서 지정된 ID까 있는 객체에 매핑하는 딕셔너리를 반환한다.

`
Blog.objects.in_bulk([1])
`

## latest()
날짜 필드로 제공된 field_name을 사용하여 테이블의 최신 객체를 나짜순으로 반환한다.
`
Entry.objects.latest('pub_date')
`
pub_date필드에 따라 테이블 최신항목을 반환한다.

## eariliest()
latest와 똑같이 동작하나 제일 오래된 항목을 반환

## first()
쿼리셋과 일치하는 첫번째 객체를 반환
`
p = Article.objects.order_by('title','pub_date').first()
`

## last()
first와 같지만 마지막 객체를 반환