#SQL 구문

구조화 된 쿼리 언어
데이터베이스를 변경,삭제,추가등이 가능

##데이터베이스 테이블

데이터베이스는 대개 하나 이상의 테이블을 포함한다.

각 테이블은 이름으로 식별된다.

테이블은 데이터가있는 레코드(행)를 포함.

**SQL 키워드는 대,소문자를 구분하지 않는다.		
ex) select는 SELECT와 같다.

##SQL의 기초 명령어
- SELECT - 데이터베이스에서 데이터를 추출한다.
- UPDATE - 데이터베이스에서 데이터를 업데이트 한다.
- DELETE - 데이터베이스에서 데이터를 삭제한다.
- INSERT INTO - 새로운데이터를 데이터베이스에 삽입한다.
- CREATE DATABASE - 새 데이터베이스를 만든다.
- ALTER DATABASE - 데이터베이스를 수정한다.
- CREATE TABLE - 새 테이블을 만든다.
- ALTER TABLE - 테이블을 수정한다.
- DROP TABLE - 테이블을 삭제한다.
- CREATE INDEX - 색인을 생성한다.
- DROP INDEX - 색인을 삭제

###SELECT

데이터베이스에서 데이터를 선택하는데 사용된다.

리턴 된 데이터는 결과 세트라고하는 결과 테이블에 저장된다.

``` 
SELECT column1, cloumn2, ...
FROM table_name1;
```

여기서 column1m cloumn2는 데이터를 선택할 테이블의 필드 이름이다.

```
SELECT * FROM table_name;
```

표에서 사용 가능한 모든필드를 선택.(전체출력)

###SELECT DISTINCT

SELECT DISTINCT는 고유한 값만 리턴하는데 사용한다.(중복값을 제외한)

```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```
중복값을 제외하여 리턴

```
SELECT COUNT(DISTINCT Country) FROM Customers;
```
중복값을 제외하여 리턴하나 데이터가 아닌 데이터의 수를 반환

###WHERE
레코드(행)절을 필터링하는 데 사용

where절은 지정된 조건을 충족하는 레코드 만 추출하는 데 사용됩니다.

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### sql에서 문자는 ''안에 사용, 숫자는 그냥 사용한다.

###WHERE에서 사용하는 연산자들

operator | description
-----|------------
=|같다
<>|다르다 (일부 sql버전에서는 !=사용)
>| 보다 클때
<| 보다 작을때
>=| 보다 크거나 같을때
<=| 보다 작거나 같을때
BETWEEN | BETWEEN A AND B(A와 B사이의 내용을 검색하라)
LIKE | LIKE 찾을내용& (or %찾을내용 or %찾을내용%)
IN | 특정 레코드값을 가져올때( IN(value1,value2))

####LIKE
WHERE절에서 열의 지정된 패턴을 찾을때 사용

**_와일드카드 문자_**

- % : 0,1 또는 복수의 문자를 나타낸다.
- _ : 한 문자를 나타낸다.

```
SELECT column1, column2...
FROM table_name
WHERE columnN LIKE pattern
```
패턴 앞뒤로 %,_를 붙여서 사용한다.
> AND, OR연산자를 사용하여 여러조건을 결합할 수 있다.	
> 백분율 기호와 밑줄은 조합해서 사용이 가능하다.

####IN
WHERE에 여러값을 지정할 수 있다.	
IN은 여러 OR의 약자

```
SELECT column_name(s)
FROM table_name
WHERE column_name IN ((SELECT사용가능) value1, value2...);
```

####BETWEEN
범위 내의 값을 선택
begin 및 end 값이 포함됨

```
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1, AND value2;
```
NOT BETWEEN을 사용하면 범위를 벗어난 값을 출력하게 한다.

##ORDER BY
결과를 오름차순 or 내림차순으로 정렬
ORDER BY는 기본적으로 오름차순 내림차순은 `DESC`사용

```
SELECT column1,column2, ...
FROM table_name
ORDER BY column1, column2, ASC|DESC
```

