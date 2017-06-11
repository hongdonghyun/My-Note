#DATABASE

##CREATE DATABASE (생성)

```
CREATE DATABASE batabase_name;
```

##DROP DATABASE (삭제)

```
DROP DATABASE database_name;
```

##CREATE TABLE
데이터베이스 안에 새 테이블을 만듬

```
CREATE TABLE table_name (
				column1 datatype,
				column2 datatype,
				column3 datatype,
				.....);
				
```

##DROP TABLE
테이블 자체를 삭제

```
DROP TABLE table_name;
```
```
TRUNCATE TABLE table_name;
```
테이블 데이터는 삭제하지만 테이블을 삭제하지는 않는다.

##ALTER TABLE
기존 테이블의 열추가,삭제,수정함

###열추가
```
	ALTER TABLE table_name
	ADD column_name datatype;
```

###열삭제
```
ALTER TABLE table_name
DROP COLUMN column_name;
```

##constraint
제약조건

CREATE TABLE로 테이블이 작성될때 또는 ALTER TABLE로 테이블이 작성된 후에 제한조건을 지정가능

``` 
CREATE TABLE table_name (
				column1 datatype constraint
				column2 datatype constraint
				);
```
##SQL제약

테이블 데이터에 대한 규칙을 지정하는데 사용
테이블에 들어갈 수 있는 데이터 유형을 제한하는데 사용

데이터의 정확성과 신뢰성이 보장
제한조건 위반시 제약

다음과 같은 제약 조건이 사용된다.

```
- NOT NULL : 열이 NULL값을 가질 수 없음을 보장
- UNIQUE : 열의 모든값이 서로 다른지 확인
- PRIMARY KEY : NOT NULL과 UNIQUE의 조합, 테이블의 각 행을 고유하게 식별
- FOREIGN KEY : 다른 테이블의 행/레코드를 고유하게 식별
- CHECK : 열의 모든 값이 특정 조건을 충족하는지 확인
- DEFAULT : 값이 지정되지 않은경우 기본값을 설정
- INDEX : 데이터베이스를 매우 신속하게 데이터생성,검색하는데 사용
```

##NOT NULL

기본적으로 열은 NULL값을 가질수 있으나 NOT NULL제약조건을 사용하면 NULL을 가질수 없게 강제하게된다.

즉, 필드에 무조건 값을 포함시켜야한다.

```
CREATE TABLE persons (
ID int NOT NULL,
bla bla bla varchar(255) NOT NULL,
);
```

##UNIQUE

값이 유일해야한다.는 제약조건

테이블에는 많은 UNIQUE제약 조건을 가질 수 있다.

사용법은 NOT NULL과 같음

###테이블이 이미 만들어진 경우에 UNIQUE제약을 걸 경우
```
ALTER TABLE persons
ADD UNIQUE (XX);
```

##PRIMARY KEY
테이블의 레코드를 고유하게 식별

기본키는 UNIQUE를 포함해야하며 NULL을 사용할 수 없다.
테이블에는 하나의 PRIMARY KEY만이 존재할 수 있다.

```
CREATE TABLE ~~~ (
				~~~~~,
				~~~~~,
				~~~~~,
				PRIMARY KEY (~~)
				);
```

##FOREIGN KEY
서로 다른 테이블을 연결하는데 사용되는 키

외래키는 다른테이블의 기본키를 참조하는 테이블의 필드 모음

##CHECK
열에 배치할 수 있는값 범위를 제한하는데 사용

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

##DEFAULT

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);
```

