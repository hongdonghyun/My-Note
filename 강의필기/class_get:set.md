#get/set

파이썬에서는 지원하지 않지만, 어떤 언어들은 외부에서 접근할 수 없는 private객체 속성을 지원한다. 이 경우, 객체에서는 해당 속성을 읽고 쓰기 위해 getter, setter메서드를 사용해야 한다.

파이썬에서는 해당 기능을 프로퍼티(property)를 사용해 간편히 구현한다.


```PYTHON
    @property #get
    def name(self):
        return self.__name

    @name.setter #set
    def name(self,new_name):
        self.__name = new_name
        print('set new name ({})'.format(self.__name))
```

**get(property)**	
속성의 값을 리턴한다.

**set(setter)**
프라이빗 처럼 내용수정이 불가하게 제약을 걸 수 있다.

##Inheritance
```
class Restaurant(Shop):
    pass
```

상속받은 클래스에서 부모 클래스의 메서드와 다른 동작을 하도록 할 수 있다.

부모 클래스 메서드에 덮어씌워 동작하게 하며 이 방법을 메서드 오버라이드(method override)라고 한다.

```
public
	외부에서 제한없이 접근/수정 가능
	
protected
	외부에서는 접근 불가능, 상속받은 클래스에서는 접근 가능
	
private
	내부에서만 접근/수정 가능
		->외부 접근 가능하도록 property사용
```

###부모 클래스의 메서드를 호출 super
```
def __init__(self,name,shop_type,address,price):
        super().__init__(name,shop_type,address)
self.price = price
```

super() 메서드를 사용해서 부모 클래스의 메서드를 호출하여 사용 (두번 타이핑 안해도된다는소리)

###다형성

```
### 다형성과 덕 타이핑
#다형성 : 동일한 실행이지만, 다른 동작을 수행할 수 있도록 허용하는 것
class User:
    def __init__(self,name):
        self.name = name

    def eat_something(self,something):
        something.eat()

    def eat_food(self,food):
        food.eat()

    def eat_drink(self,drink):
        drink.eat()

class Something:
    def __init__(self,name):
        self.name =name

    def eat(self):
        print('{}는 무엇인지 몰라 먹을 수 없다!'.format(self.name))

class Food(Something):
    def eat(self):
        print('{}을 먹었다 배가부르다!'.format(self.name))

class Drink(Something):
    def eat(self):
        print('{}을 마셨다. 갈증이 해소됐다!'.format(self.name))
```