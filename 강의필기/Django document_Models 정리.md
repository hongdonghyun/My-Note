#Models
모델이란 django에서 DB(테이블과 필드)를 관리할 수 있는 모듈이다.

##예시
```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
위의 예시는 밑에 있는 SQL문의 구조와 같다.

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```
django에서 모델을 사용하기 위해서는
projectnamefolder의 settings.py파일의 ```INSTALLED_APPS```속성에 사용하는 app을 넣고
```	
./manaege.py makemigrations```
를 실행해야한다.

##field
###null

```

기본값은 False이며 True일 경우 DB에 

NULL값을 넣을 수 있다. 
```

###blank

```
기본값은 False이며 True일 경우 빈 문자열 ""이 들어간다
```

###null과 blank의 차이
null은 값이 없다는 뜻이지만
blank는 빈 문자열이 들어가 있다.

###choice
튜플이 담겨있는 리스트가 전달이 되면 선택가능항목이 된다.

```
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


셸에서 입력할 때
from blog.models import Person

p = Person(
name="Fred Flintstone", shirt_size="L"
)

p.save()
p.shirt_size
p.get_shirt_size_display()
```
###default
필드의 기본값을 정할수 있다.

###help_text

```
help_text="Please use the following format: <em>YYYY-MM-DD</em>."
```
###primary_key
Django는 기본 키를 보유 할 자동 필드를 자동으로 추가하므로 해당 필드를 재정의하려는 경우를 제외하고는 모든 필드에서 ```primary_key = True```를 설정하지 않아도 된다.

```primary_key = True```는
 ```null = False 및 unique = True```를 의미한다.

하나의 기본 키만 객체에 허용되며 기본 키 필드는 읽기 전용이다.

###unique
참이면 필드는 테이블 전체에서 고유해야한다. **유일성**


###verbose_name
필드명을 지정하지 않았을 경우 ```ForeignKey```,```ManyToManyField```,```OneToOneField```를 제외한 필드는 자동으로 변수명을 입력해주지만 
```verbose_name```변수에 입력해둔다면 원하는 값으로 지정할 수 있다.

예시)

```
first_name = models.CharField("person's first name", max_length=30)

last_name = models.CharField(max_length=30)
```
```first_name의 verbose_name```은 **"preson's first name"**이 되고

```last_name의 verbose_name```은 **"last_name"**이 된다.

`ForeignKey`,`ManyToManyField`,`OneToOneField`의 경우 `verbose_name`이라는 인자를 사용하여 직접 지정해야한다.

예시)

```
poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)
```

##Relationsship
Django는 다대일,다대다,일대일 데이터베이스 관계를 제공한다.

- Many To One (다대일)
- Many To Many (다대다)
- One To One(일대일)

###Many to one 
다대일 관계를 정의하려면

django.db.models.ForeignKey를 사용해야한다.

선언은 일반 필드처럼 선언하면 된다.

```
예시)
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
```
자동차를 만드는 공장에서 여러종류의 자동차를 만들기 때문에 car필드에서 외래키를 가진다.
>다대일 관계는 항상 '다'쪽에 외래키가 존재하며 양방향 관계는 항상 서로를 참조해야한다.

### Many to Many

다대다 관계를 사용하려면 Many To ManyField를 사용해야한다.

```
예시)
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```
피자에는 여러개의 토핑이 올라간다.
토핑 또한 여러피자에 올라갈 수있으므로 위와같은 예시를 보여준다.
> ManyToManyField는 서로 참조 하는 관계 두 필드중 하나에만 들어가야한다.
> 
> 일반적으로 편집해야할 필드에 들어간다. 
> (피자위에 올라가는 토핑을 수정하는게 더 자연스럽다)

**이번에는 다대다 관계중 세부과정이 필요한 복잡한 다대다 관계를 살펴보자**

```
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

중간에 끼여있는 모델이 있는 다대다 관계이다.

사람들은 그룹에 속해 있지만
사람들의 이름,소속,가입날짜,초청이유등을 원하고 있다.
>눈여겨 볼점은 그룹필드에서 ManyToManyfield를 선언하고 parameter로 through를 사용하고 있다는 점이다.

>through변수를 사용하여 Membership필드를 참조하고 있다.

###One To One

일대일 관계를 사용하려면 `OneToOneField`를 정의하면 된다.

예를 들어, 어떠한 장소의 데이터베이스를 구축했다면 데이터베이스에 주소, 전화 번호 등과 같은 표준적인 물건을 만들 수 있습니다. 
레스토랑의 데이터베이스를 구축하고 레스토랑 모델에서 해당 필드를 복제하는 대신 레스토랑을 "OneToOneField"로 만들 수 있습니다.	
사실, 이것을 처리하기 위해 암시 적 일대일 관계가 포함 된 '상속'을 일반적으로 사용합니다.

##Model across files

다른 앱에서 사용하고 있던 모델을 가져와서 다른앱에서 다시 재사용이 가능하다.

```
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
```
지오그래피에 있는 모델에서 집코드라는 클래스를 참조했다.
(일단 적기는 했으나 너무 당연한 부분이라..)

##Field name restrictions

네이밍 룰이다.

Django에서는 두가지의 제한이 있다.

1. 파이썬 자체 예약어는 사용금지
2. (__) double underscore 사용한다면 Django가 쿼리내에서 검색을 하기 시작한다.

>SQL의 예약어는 사용가능하다. Django안에서 필드선언은 SQL문밖에서 실행하기 때문이다.

##Custom field type
[필요할때 찾아서 보자](https://docs.djangoproject.com/en/1.11/howto/custom-model-fields/)

##Meta options
MetaData를 주기 위해선 클래스안에 `class Meta`를 선언하여 포함시킨다.

예시)

```
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
```

MetaData를 추가하는건 필수가 아닌 선택이다.

주고싶은 옵션은 아니지만 필요한것들
정렬방식이나,이름같은것들이 될것이다.

##Model attributes

###objects
우리가 무심결에 사용하고 있었던 objects가 매니저다

예시)
`Post.objects.all()` 
`Post.objcets.create(something)`

특별히 지정해 주지않는한 `objects`로 사용하면 된다.

##Model methods

뭔말인지 모르겠으니 닥치고 예시부터 뜯어보자

```
rom django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```

일반적인 클래스 선언인데
django를 배우던중 property가 처음으로 튀어 나왔다.

아무래도 문서에서는 무언가를 실행하기 위해서는 custom method를 이용해야한다는걸 말하는것 같다.
`@property`또한 우리가 사용하고 있던 method였다.

자세한 설명은 다음에 추가해보기로 하고
중요하다고 설명하는 몇가지 명령을 알아보고자 한다.

- `__str__`(python3)
- `__unicode__`(python2)
- `get_absolute_url()`

`__str__`은 강제로 표시하는거 콘솔이나 관리자들이 체크할때 쓰기편하다
`get_absolute_url()`은
Django에게 url을 어떻게 불러와야하는지 알려주는 method이다.
고유한 url을 가진 object들은 `get_absolute_url()`을 반드시 정의해줘야 한다.

##Model inheritance
Django또한 클래스 상속이 가능하다.
python과 동일하게 사용가능하나
Django안의 룰을 따라야 한다.
` django.db.models.Model.`를 써라!

부모모델이 단독으로 사용되는 모델이 될지
자식모델을 통하여 사용할 수 있는 정보를 보유할지를 결정한다.

Django에서는 세가지 방법의 상속이 가능하다.

1. 부모클래스에 정보를 입력하여 자식클래스에 자동으로 데이터를 갖게 하고자 한다면 기본 추상클래스를 사용하면 된다.

2. 기존 모델을 하위 클래스화 하고 각각의 모델에 고유 데이터베이스를 가지고자 한다면 다중 테이블 상속을 사용한다.

3. 모델 필드를 변경하지 않고 파이썬수준의 동작만 수정하려는 경우 Proxy모델을 사용한다.


###Abstract base classes
추상클래스 상속

추상 클래스는 공통된 정보를 다른 모델에게 뿌릴때 유용하다.

기본 클래스를 작성하고 메타클래스를 작성하여 `abstract = True`로 할당한다면
추상화가 가능하며 이 클래스는 데이터베이스가 형성되지 않는다.
>abstract의 default는 False다

```
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
``` 

###Multi-table inhreitance
상속 받고자하는 모델이 모두 하나의 모델일때
OneToOnefield속성을 사용하여 상속 할 수있다.

```

from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
 
```
###Proxy model
데이터베이스를 생성하지 않고 파이썬 기능만을 사용한 상속을 할때 사용된다.
>if문이라던지 for라던지..

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
```
내부에 메타클래스를 선언하고 `proxy`를 `true`로 선언하면 된다.

- 메타데이터 상위에 있는 MyPerson은 Person클래스와 같은 데이터베이스 테이블에서 동작한다.
- proxy model은 추상클래스가 아닌모델을 상속 받아야 한다.
- proxy model은 다른 데이터베이스 사이에 연결을 제공하지 않으므로 여러개의 비 추상 모델을 상속 받을 수 없다.
- 그러나 proxy model은 model field를 정의하지 않으면 추상클래스를 상속 받을 수 있다.
- 공통의 비 추상모델 클래스를 공유하는 proxy model로 부터 상속 할 수 있다.

proxy model에 manager를 따로 설정 하지않는다면 부모의 manager를 상속 받는다.

###Multiple inheeritance
간단하다.

```
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...

class BookReview(Book, Article):
    pass
```
여러개를 받는것이 다중상속이다.




