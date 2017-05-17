#변수

##변수타입 확인
내장함수 `type`

###변수 이름의 제한

- 소문자
- 대문자
- 숫자
- 언더스코어(_)	
 -언더스코어는 일반적으로 사용하지 않음(보이지 않는 파일등에 사용)
- 예약어

#연산
- % : 나머지
- / : 나누기
- //: 정수 나누기
- ** : 지수연산(제곱)
- () : 우선순위

#문자열
- \' : 작은따옴표
- \" : 큰따옴표

## 슬라이스 연산

[start:end:step]

## 길이
	`len` 함수 사용

###문자열 나누기
`split`사용	
 `xxxx = '내용'.split()`을 하여 쉽게 리스트 생성 가능
 
###문자열 합치기
```
>>> girlsday_list = girlsday.split(',')
>>> girlsday_str = ', '.join(girlsday_list)
>>> print(girlsday_str)
민아, 유라, 소진, 혜리
```

###대소문자
- xxx.capitalize() :첫문자만 대문자
- xxx.title() : 띄워쓰기로 나눠진 첫문자 대문자
- xxx.lower() : 전체 소문자
- xxx.swapcase() : 반전

##.format

`{}.format(변수)`

#list []
배열이랑 같음

```
empty_list1 =[]
empty_list2 =list()
```

##extend
리스트 합치기, +=한거랑 같다.
`xxx.extend(xxx2)`

###append랑 차이
 extend대신 append를 사용하면 특정 위치에 **리스트**가 추가됨
 
##리스트 특정위치에 항목추가
`list.insert(index,obj)`

##특정 위치 리스트 항목 삭제
`del xxx[x]`

###값으로 리스트 항목 삭제
`xxx.remove('str')`

###리스트 항목 추출 후 삭제
`xxx.pop(index)` (값을 리턴하고 삭제한다)

###count
xxx.count('val')
순서값을 리턴

### 정렬 (sort)
- sort는 리스트를 자체 정렬 (리턴안함)
- sorted 리스트를 정렬해서 리턴값으로 준다.

# tuple ()
`empty_tuple = ()`
하나의 값만 넣을시 **,** 필요

## tuple unpacking
`x1,x2 ... = 튜플`
개수 맞아야함

#딕셔너리 {}
key - value 형태로 항목을 가지는 구조
형변환 **dict**함수 사용
```
empty_dict ={}

empty_dict= dict()
```

###key 값으로 찾기
`xxx['key']`

###update(결합)
`xxx(원본).update(xxx(합칠것))`
**같은키가 존재한다면 update로 주어진 딕셔너리 우선**

#### del
del xxx['key']

### keys() 모든키

### values() 모든 값

### items() 모든 키-값(튜플 반환)

###copy() 복사

#set
키만 있는 딕셔너리 중복값 X
`empty_set = set()`

empty_set = {'xxx','xxx','xxx'}
value 없이 딕셔너리처럼 써도 set

##형변환
문자열,리스트,튜플,딕셔너리를 셋으로 변환할 수 있으며 중복된 값이 사라진다.

#집합연산

연산자|설명
-----|----------
`|` | 합집합(union)
&|교집합(inertsetion)
-|차집합(difference)
^|대칭차집합(exclusive)
<=|부분집합(subset)
<|진부분집합(proper subset)
>=|상위집합(superset)
>|진상위집합(proper superset)

# if
if 조건:

```
if 조건:
	내용
else:
	 내용
	 
if 조건1:
	조건1 true
elif: 조건2:
	조건1 false, 조건2 true
else:
	조건1, 조건2 false
```

# for
```
for (for문에서 사용할 변수이름) in 순회가능 객체:
```

# zip
zip(순회가능객체1,순회가능객체2)

#range (범위지정)
`range(start,stop,step)`
	

