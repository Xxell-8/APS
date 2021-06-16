# 07. Database



## 1. SQL

> SQL(Structured Query Language)이란, 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

- SQL 문법 종류
  - DDL (데이터 정의 언어)
    - CREATE
    - DROP
    - ALTER
  - DML (데이터 조작 언어)
    - INSERT
    - SELECT
    - UPDATE
    - DELETE
  - DCL (데이터 제어 언어)
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK



## 2. Database 생성

- `sqlite3`를 활용해 파일을 불러오거나 생성

  - 해당하는 DB 파일이 있으면 찾고, 없으면 새로 생성

  ```sqlite
  $ sqlite3 DBname		 -- 1. 콘솔로 DB를 열고
  sqlite > .databases		 -- 2. DB 목록 확인
  ```



- CSV 파일 불러오는 명령어

  ```sqlite
  sqlite > .mode csv
  sqlite > .import filename.csv tablename
  -- ex. sqlite> .import example.csv examples
  ```

  - cf. `.`으로 시작하는 모든 명령어는 sqlite3 프로그램 기능을 실행하는 명령어

    ​    👉 SQL 문법에는 속하지 않는다!



## 3. 테이블 생성 및 삭제

#### 1. Data Type

- SQLite는 동적 데이터 타입으로, 기본적으로 유연하게 데이터가 입력

  |  Type   |                                                              |
  | :-----: | :----------------------------------------------------------: |
  | INTEGER | INT(4bytes), TINYINT(1bytes), SMALLINT(2bytes), MEDIUMINT(3bytes), BIGINT(8bytes), UNSIGNED BIG INT |
  |  TEXT   |              CHARACTER(20), VARCHAR(255), TEXT               |
  |  REAL   |                     REAL, DOUBLE, FLOAT                      |
  | NUMERIC |          NUMERIC, DECIMAL, BOOLEAN, DATE, DATETIME           |
  |  BLOB   |                    no datatype specified                     |

  

#### 2. `CREATE` 👉 테이블 생성

```sql
CREATE TABLE table (
  column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);
```

- `INTEGER PRIMARY KEY` 타입으로 컬럼 생성시 기본 `rowid` 를 대체함
  - PRIMARY KEY를 따로 작성하지 않으면, rowid가 자동 입력
  - **단, PRIMARY KEY는 INTEGER 타입에서만 사용가능**

- 컬럼 별로 `NOT NULL` 조건 추가 가능

  ```sql
  CREATE TABLE table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    ...
  );
  ```
  - **`AUTOINCREMENT`** 설정을 하면 삭제된 데이터의 pk를 재사용하지 않음

  

- 생성한 테이블과 스키마 조회

  ```sqlite
  sqlite> .tables          -- 테이블 목록 조회
  sqlite> .schema tablename    -- 특정 테이블 스키마 조회
  ```

  

#### 3. `DROP` 👉 테이블 제거

```sqlite
sqlite> DROP TABLE tablename;
sqlite> .tables -- 테이블 제거 확인
```



## 4. 데이터 CRUD

#### 1. `INSERT` 👉 데이터 추가

- 기본적인 추가 방법

  ```sql
  -- 1. record 1개 추가
  INSERT INTO table (column1, column2)
  VALUES (value1, value2);
  
  -- 2. record 여러 개 추가
  INSERT INTO table (column1, column2)
  VALUES (value1, value2), (value1, value2), (value1, value2);
  ```

  

- PK를 추가했을 경우

  ```sql
  INSERT INTO table (column1, column2)
  VALUES (value1, value2);
  
  INSERT INTO table
  VALUES (1, value1, value2);
  ```

  

#### 2. `SELECT`

```sql
-- 모든 컬럼 가져오기 --
SELECT * FROM table;

-- 특정 컬럼 가져오기 --
SELECT column1, column2 FROM table;

-- LIMIT: 원하는 개수(num)만큼 가져오기 -- 
SELECT column1, column2
FROM table
LIMIT num;

-- OFFSET: 특정 위치에서부터 가져올 때 --
-- (맨 위부터 num만큼 떨어진 값부터 가져온다는 의미)
SELECT column1, column2
FROM table
LIMIT num OFFSET num;

-- WHERE: 조건을 통해 값 가져오기 --
SELECT column1, column2
FROM table
WHERE column=value;

-- DISTINCT: 중복없이 가져오기 -- 
SELECT DISTINCT column FROM table;

-- Q.users에서 age가 30이상인 사람만 가져온다면? --
SELECT * FROM users
WHERE age >= 30;

-- Q.users에서 age가 30이상인 사람의 이름만 가져온다면? --
SELECT first_name FROM users
WHERE age >= 30;

-- Q.users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 가져온다면? 
SELECT age, last_name FROM users
WHERE age >= 30 and last_name='김';
```



#### 3. `DELETE`

```sql
DELETE FROM table
WHERE condition;

-- ex)
DELETE FROM classmates
WHERE name='Tom';
```



#### 4. `UPDATE`

```sql
UPDATE table
SET column1=value1, column2=value2, ...
WHERE condition;

-- ex)
UPDATE classmates
SET name='Tom', address='Seoul'
WHERE name='Tommy';
```



## 5. SQL 추가 기능

#### 1. Expressions

- COUNT

  ```sql
  SELECT COUNT(*) FROM users;
  ```

- AVG

  ```sql
  SELECT AVG(age)
  FROM users
  WHERE age >= 30;
  ```

- MAX, MIN, SUM



#### 2. LIKE

- LIKE에서 활용할 수 있는 와일드 카드는 두 가지

  -  `_` 👉 반드시 해당 위치에 한 개의 문자가 존재

    ```sql
    -- 20대인 사람들만 가져올 때 --
    SELECT *
    FROM users
    WHERE age LIKE '2_';
    ```

  - `%` 👉 해당 위치가 0개 이상의 문자열이 존재

    ```sql
    -- 지역번호가 02인 사람만 가져올 때 --
    SELECT *
    FROM users
    WHERE phone LIKE '02-%';
    ```

    

#### 3. ORDER BY

```sql
-- ASC: 오름차순(생략 가능) / DESC: 내림차순 --
SELECT columns FROM table
ORDER BY column1, column2 ASC | DESC;

-- 나이, 성 순서로 오름차순 정렬하여 상위 10개만 뽑아보면? --
SELECT * 
FROM users
ORDER BY age, last_name
LIMIT 10;
```



#### 4. GROUP BY

- 지정된 기준에 따라 행 세트를 그룹으로 결합

  - 데이터 요약에 유용

  ```sql
  SELECT column1, aggregate_function(column_2)
  FROM table
  GROUP BY column1, column2;
  
  -- 성(last_name)씨가 몇 명인지 조회할 때 --
  SELECT last_name, COUNT(*)
  FROM users
  GROUP BY last_name;
  ```

  

#### 5. ALTER

- 테이블 이름 변경

  ```sql
  ALTER TABLE oldname
  RENAME TO newname;
  ```

- 새로운 컬럼 추가

  ```sql
  ALTER TABLE table
  ADD COLUMN column datatype;
  ```

  

## 6. SQL with Django ORM

#### 1. 기본 CRUD

- 전체 레코드 조회

  ```python
  # ORM
  User.objects.all()
  ```

  ```sql
  -- SQL
  SELECT * FROM users_user;
  ```

- 레코드 생성

  ```python
  # ORM
  User.objects.create(
  first_name='Harry',
  last_name='Porter'
  )
  ```

  ```sql
  -- SQL
  INSERT INTO users_user
  VALUES ('Harry', 'Porter');
  
  INSERT INTO users_user (first_name, last_name)
  VALUES ('Harry', 'Porter');
  ```

- 특정 레코드 조회

  ```python
  # ORM
  User.objects.get(pk=1)
  ```

  ```sql
  -- SQL
  SELECT * FROM users_user
  WHERE id=1;
  ```

- 특정 레코드 수정

  ```python
  # ORM
  user = User.objects.get(pk=2)
  user.first_name = 'Tom'
  user.save()
  ```

  ```sql
  -- SQL
  UPDATE users_user
  SET first_name='Tom'
  WHERE id=2;
  ```

- 특정 레코드 삭제

  ```python
  # ORM
  User.objects.get(pk=1).delete()
  ```

  ```sql
  -- SQL
  DELETE FROM users_user
  WHERE id=1;
  ```



#### 2. 조건에 따른 쿼리문

- 전체 인원 수 조회

  ```python
  # ORM
  User.objects.count()
  ```

  ```sql
  -- SQL
  SELECT COUNT(*) FROM users_user;
  ```

- 조건에 맞는 사람의 이름 조회

  ```python
  # ORM
  User.objects.filter(condition).values('first_name')
  ```

  ```sql
  -- SQL
  SELECT first_name FROM users_user
  WHERE condition;
  ```
  - 대소 관계 활용 👉 `__gte` , `__lte` , `__gt`, `__lt`

    ```python
    # 30세 이상인 사용자의 인원 수
    User.objects.filter(age__gte=30).count()
    ```

  - 조건이 여러 개일 경우

    - AND 연산은 나열하면 되지만 OR 연산은 `Q`를 활용

      ```python
      # AND
      User.objects.filter(age=30, last_name='김')
      # OR
      from django.db.models import Q
      User.objects.filter(Q(age=30) | Q(last_name='김'))
      ```

      

#### 3. 정렬

- 나이 많은 순으로 10명

  ```python
  # orm
  User.objects.order_by('-age')[:10]
  ```

  ```sql
  -- sql
  SELECT * FROM users_user
  ORDER BY age DESC
  LIMIT 10;
  ```

- 잔고 오름차순 + 나이 내림차순 10명

  ```python
  # orm
  User.objects.order_by('balance', '-age')[:10]
  ```

  ```sql
  -- sql
  SELECT * FROM users_user
  ORDER BY balance, age DESC
  LIMIT 10;
  ```

- 이름 오름차순으로 5번째인 사람

  ```python
  # orm
  User.objects.order_by('first_name')[4]  
  ```

  ```sql
  -- sql
  SELECT * FROM users_user
  ORDER BY first_name
  LIMIT 1 OFFSET 4;
  ```

  

#### 4. Expression

- LIKE in ORM 👉 `__contains`, `__startswith`, `endswith`

  - 전화번호에 123이 포함된 사람

    ```python
    User.objects.filter(phone__contains='123')
    ```

    ```sql
    SELECT * FROM users_user
    WHERE phone LIKE '%123%'
    ```

  - 전화번호가 010으로 시작되는 사람들의 거주 지역을 중복없이 조회

    ```python
    User.objects.filter(phone__startswith='010').values('country').distinct()
    ```

    ```sql
    SELECT DISTINCT country FROM users_user
    WHERE phone LIKE '010-%'
    ```

    

- `aggregate`

  > - 지정한 조건에 맞는 값을 Key: Value 값의 딕셔너리로 반환
  > - 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용

  - 전체 평균 나이

    ```python
    # orm
    User.onjects.aggregate(average_age=Avg('age'))
    ```

    ```sql
    -- sql
    SELECT AVG(age) FROM users_user;
    ```

  - 서울에 거주하는 사람의 평균 계좌 잔고

    ```python
    # orm
    User.objects.filter(region='Seoul').aggregate(Avg('balance'))
    ```

    ```sql
    -- sql
    SELECT AVG(balance) FROM users_user
    WHERE region='Seoul';
    ```

- `annotate`

  > - 지정한 조건에 맞는 값을 새로운 쿼리셋으로 생성
  > - 새로운 필드를 만들어 내용을 채워넣는, 즉 컬럼 하나를 추가하는 것

