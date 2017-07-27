# Data_structure

pip install matplotlib

## Day1
- linear search
- binary search
- big O of linear search
- big O of binary search

### 자료구조와 알고리즘

#### 자료구조
데이터를 저장하고 탐색하는 방법에 대한 고민들

1. insert (어떻게 저장할 것인가?)
2. search (어떻게 탐색 할 것인가?)
3. delete (어떻게 지울것인가?)

#### 알고리즘

문제해결 방법

### array 와 linked list

배열의 원리

동일한 자료형을 가진 변수형의 모임


## 재귀함수

### factorial,fibo

```
def fibo(n):
    if n <= 1:
        return 1

    return fibo(n - 2) + fibo(n - 1)


for i in range(5):
    print(fibo(i), end=' ')


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)


def fibo_gen(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    f = fibo_gen(10)
    for i in range(10):
        print(next(f), end=' ')
```

### 하노이의탑

```
def hanoi(num, _from, _by, _to):
    if num == 1:
        print('이동 {}에서 {}로 {}번째 원반을 이동'.format(_from, _to, num))

        return
    hanoi(num - 1, _from, _to, _by)
    print('이동 {}에서 {}로 {}번째 원반을 이동'.format(_from, _to, num))
    hanoi(num - 1, _by, _from, _to)


while(1):
    _input = int(input("원반의 개수를 입력하세요 "))
    if _input == 0:
        break
    hanoi(_input,'a','b','c')
```

### linear search


## big O 표기법

1. O(1)
	- array[n] 
2. O(N)
	- 
3. O(logN)
4. O(NlogN)
5. O(N^2)