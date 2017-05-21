#SQL문

[튜토리얼 사이트](https://www.w3schools.com/)

##INSERT INTO

테이블에 새로운 레코드를 삽입할때 사용

두 가지 방법으로 INSERT INTO문을 작성 할 수 있다.

1. 열 이름과 삽일 할 값 모두 지정

```
INSERT INTO table_name (column1, column2, column3...);
VALUES (value1, value2, value3);
```

2. 특정열에만 데이터 삽입

INSERT INTO Customers (CustomerName, City, Country)

VALUES ('bla,blabla');

##NULL

```
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```
### IS NOT NULL

```
SELECT LastName, FirstName, Adderss
FROM Persons
WHERE Address IS NOT NULL;
```

주소가 있는 모든사람 출력

##UPDATE
테이블에 있는 기존 레코드를 수정하는데 사용.

```
UPDATE table_name
SET column1 = value1, column2 = value2,
WHERE condition;
```

###여러 레코드 업데이트

업데이트 될 레코드의 수를 결정하는것은 WHERE 절이다.

```
UPDATE Customers
SET ContactName ='juan'
WHERE Country = 'Mexico';
```
멕시코인 레코드에 대해 연락처이름을 준으로 업데이트

**만약 레코드 업데이트시 WHERE절을 생략하면 모든 레코드가 업데이트 된다.**

##DELETE
```
DELETE FROM table_name
WHERE condition;
```

**WHERE절을 생략하면 모든 레코드가 삭제된다.**

##SELECT TOP
SELECT TOP절은 리턴할 레코드 수를 지정하는데 사용

```
SELECT TOP  (number|precent) * column_name(s)
FROM table_name
WHERE condition;
```

##MIN() MAX()
선택된 열의 가장 작은값,큰값을 리턴

```
SELECT MIN or MAX (column_name)
FROM table_name
WHERE condition;
```

##COUNT(), AVG() SUM()
- COUNT() : 지정된 조건과 일치하는 행 수를 반환
	
	```
	SELECT COUNT (column_name)
	FROM table_name
	WHERE condition;
	```
	
- AVG() : 숫자 열의 평균값을 반환
	
	```
	SELECT AVG(column_name)
	FROM table_name
	WHERE condition;
	``` 
- SUM() : 숫자열 총 합계를 반환
	
	```
	SELECT SUM(column_name
	FROM table_name
	WHERE condition;
	```

##alias
테이블 또는 테이블의 컬럼에 임시 이름을 제공하는데 사용한다.
별명을 조회 기간동안만 생존

열에서 사용시

``` 열에서 사용시
SELECT column_name AS alias_name
FROM table_name;
```

테이블에서 사용시

```테이블에서 사용시
SELECT column_name AS alias_name(s)
FROM table_name AS alias_name;
```

- 퀘리에 두 개 이상의 테이블이 관련 되어있을때
- 열이름이 길거나 읽기 힘들때
- 두개이상의 열이 결합되었을때

##JOIN
두개이상의 테이블의 행을 합칠때

[조인 너무 어려움 이거봐라](https://www.w3schools.com/SQL/sql_join.asp)

##UNION
두개 이상의 SELECT문과 결과 집합을 결합하는데 사용

조건

- SELECT문은 같은 수의 열을 가져야한다.
- 열은 유사한 데이터 형식을 가져야 한다.
- SELCET문의 열은 동일한 순서로 있어야한다.

```
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2
```
