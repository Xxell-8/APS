# 02. Django Model



## 1. Model

- 웹 어플리케이션의 데이터를 구조화하고 조작하기 위한 도구
  - 모델은 단일한 데이터에 대한 정보를 가짐
  - 일반적으로 각각의 모델(클래스)는 하나의 데이터베이스 테이블과 매핑
  - 부가적인 메타데이터를 가진 DB의 구조(layout)를 의미



####  1. Database

- `Query`
  - 데이터를 조회하기 위한 명령어
  - (주로 테이블형 자료구조에서) 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- `Schema` 👉 Structure
  - DB에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
  - DBMS(DB 관리 시스템)가 주어진 설정에 따라 DB 스키마를 생성
    - 사용자가 자료 저장·조회·삭제·변경할 때 DB 스키마를 참조하여 명령 수행
- `Table` 👉 Relation
  - 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
  - `field`: 속성, column
    - 모델 안에 정의한 클래스에서 클래스 변수
  - `record`: 튜플, row
    - ORM을 통해 해당하는 필드에 넣은 데이터
  - cf. `PK`(기본키)
    - 각 레코드의 고유 값 👉 Primary Key



####  2. ORM

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에(Django - SQL)데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- 장단점

  | 장점                                                         | 단점                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | - SQL을 몰라도 DB 연동 가능<br />- SQL의 객체지향적 접근으로 **생산성 증가**<br />- ORM은 독립적으로 작성 + 해당 객체는 재활용 가능<br />  👉 모델에서 가공된 데이터를 view에 의해 template과 합쳐지는 형태로 디자인 패턴을 견고하게 다지는 데에 유리 | - ORM만으로 완전한 서비스 구현은 어려움<br />- 프로젝트의 복잡성이 커질 경우, 설계 난이도 상승 |

- 객체 지향 프로그래밍에서 DB를 편리하게 관리하기 위해 ORM 프레임워크 도입
  - 즉, **DB를 객체로 조작하기 위해 ORM을 사용하는 것!**



#### 3. Data 생성

- `models.py` 작성

  ```python
  # app_name/models.py
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField() 
  ```

  - 모델 클래스는 models.Model 상속
  - `id`는 테이블 생성시, 자동으로 만들어짐
  - `title`과 `content`는 클래스 변수로, 모델의 field를 나타냄
    - field는 클래스 속성으로 지정, 각 속성은 각 DB의 열에 매핑

- `Model Field`

  - `CharField(max_length=None, **options)` 
    - 길이 제한이 있는 text 필드에 사용
  - `TextField(**options)` 
    - 길이 제한이 없는 text 필드 👉 글자 수가 많을 때 사용
  - `DateTimeField(auto_now=False, auto_now_add=False, * *options)`
    - `auto_now` : 객체가 저장될 때마다 자동으로 필드를 세팅 (최종 수정 일자)
    - `auto_now_add`: 처음 저장될 때만 필드를 세팅(최초 생성 일자)
  - [+ more](https://docs.djangoproject.com/en/3.1/ref/models/fields/)



## 2. Migrations

- django가 model에 생긴 변화(필드 추가, 모델 삭제 등)를 반영하는 방법

- **3 STEP in Model-DB** 

  ① `models.py` : 변경사항 발생 (생성 / 수정)

  ② `makemigrations` : migration 파일 만들기 (설계도)

  ③ `migrate` : DB에 적용 (테이블 생성)



####  1. `makemigrations`

- model 변경사항에 기반하여 새로운 migration(ORM에 보낼 설계도)을 만들 때 사용

- model 활성화 전, DB 설계도(migration) 작성

  ```bash
  $ python manage.py makemigrations
  ```



####  2. `migrate`

- 설계도를 실제 DB에 반영하는 과정

  -  `makemigrations` 로 만든 설계도를 실제 `db.sqlite3` DB에 반영

- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

  ```bash
  $ python manage.py migrate
  ```



####  3. etc.

- `sqlmigrate`

  - migration에 대한 SQL 구문을 보기 위해 사용
  - 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 가능

  ```bash
  $ python manage.py sqlmigrate app_name 0001
  ```

- `showmigrations`

  - 프로젝트 전체의 migration 상태를 확인하기 위해 사용
  - migrations 설계도들이 migrate 됐는지 안됐는지 확인 가능

  ```bash
  $ python manage.py showmigrations
  ```



## 3. Database API

> - DB를 조작하기 위한 도구
> - Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도와줌



#### 1. DB API 구문

- Making Queries

  |  Article.  | object. |    all()     |
  | :--------: | :-----: | :----------: |
  | Class Name | Manager | QuerySet API |

  - **`objects` Manager**

    - Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
    - Model Manager와 Django Model 사이의 **Query 연산의 인터페이스 역할** 을 해줌
      - 즉, `models.py` 에 설정한 클래스(테이블)을 불러와서 사용할 때, 
        - DB와의 interface 역할 수행
    - 모든 Django 모델 클래스에 대해 `objects` 라는 Manager(django.db.models.Manager) 객체를 자동으로 추가 👉 Manager(objects)를 통해 특정 데이터를 조작

    

  - **QuerySet**
    - 데이터베이스로부터 전달받은 객체 목록
      - queryset 안의 객체는 0개, 1개, 혹은 여러 개일 수 있음
    - 데이터베이스로부터 데이터 조회, 필터, 정렬 등을 수행
      - Query를 DB에 던져, CRUD



#### 2. etc.

- **QuerySet API**
  - 데이터베이스 조작을 위한 다양한 QuerySet API method
    - QuerySet을 주는 기능
    - QuerySet이 아닌 객체(단일 객체 등)를 주는 기능
  - [QuerySet API Docs](https://docs.djangoproject.com/en/3.1/ref/models/querysets/)

- Django shell

  - 일반 파이썬 쉘을 통해서는 Django 프로젝트 환경에 접근 불가

    👉 Django 프로젝트 설정이 로딩된 파이썬 쉘 활용

    ```bash
    $ pip install ipython django-extensions
    ```

    ```python
    # settings.py
    
    INSTALLED_APPS = [
        ...
        'django_extensions',
        ...
    ]
    ```

    ```bash
    $ python manage.py shell_plus
    ```

- [참고] ORM이 변환한 SQL문 보기

  ```python
  >>> sample = Article.objects.all()
  >>> str(sample.query)
   👉 SELECT 
  	"articles_article"."id", "articles_article"."title", "articles_article"."content", 
      "articles_article"."created_at", "articles_article"."updated_at" 
  	FROM 
  	"articles_article"
  ```



## 4. CRUD in shell_plus

> - 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create, Read, Update, Delete



```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



####  1. CREATE

- 데이터 객체를 생성하는 3가지 방법

  ```python
  # 1. 인스턴스 생성 후 인스턴스 변수 할당 👉 DB 저장
  >>> article = Article()
  >>> article.title = 'Title_1'
  >>> article.content = 'Content_1'
  >>> article.save()
  
  # 2. 인스턴스 생성 시 인스턴스 변수 할당 👉 DB 저장
  >>> article = Article(title='Title_2', content='Content_2')
  >>> article.save()
  
  # 3. create() 활용 👉 바로 DB에 저장
  >>> Article.objects.create(title='Title_3', content='Content_3')
  
  ## DB 확인
  >>> Article.objects.all()
  <QuerySet [<Article: Title_1>, <Article: Title_2>, <Article: Title_3>]>
  ```

  

####  2. READ

- 다양한 조건을 통해 원하는 데이터를 조회하는 것이 중요
  - `all()`

    - DB에 있는 전체 `QuerySet`을 return

    ```python
    >>> Article.objects.all()
    <QuerySet [<Article: Title_1>, <Article: Title_2>, <Article: Title_3>]>
    ```

  - `get()`

    - 조건에 맞는 하나의 객체를 return
      - `unique` 혹은 `Not Null` 특징을 가진 속성(ex. `pk`)으로 접근 
      - 해당 객체가 없을 경우, `DoesNotExist` 에러
      - 해당 객체가 여러 개일 경우, `MultipleObjectReturned` 에러

    ```python
    # 해당 객체가 없는 경우
    >>> Article.objects.get(pk=100)
    DoesNotExist: Article matching query does not exist.
    
    # 해당 객체가 여러 개인 경우
    >>> Article.objects.get(content='django!')
    MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
    ```

  - `filter()`

    - 지정한 조회 매개 변수와 일치하는 객체를 포함한 새로운 `QuerySet`을 return

    ```python
    >>> Article.objects.filter(content='django!')
    <QuerySet [<Article: Title_1>, <Article: Title_2>]>
    
    >>> Article.objects.filter(title='first')
    <QuerySet [<Article: first>]>
    ```

    - Field Lookups

      - SQL WHERE절(조건문) 지정 방법

      - QuerySet 메서드 `filter()`, `exclude()` 및 `get()`에 대한 키워드 인수로 지정

        ```python
        # gt(greater than) pk=1
        Article.objects.filter(pk__gt=1)
        ```

        

- [참고] `pk` lookup shortcut

  - `.get(id=1)` 형태 뿐만 아니라 `.get(pk=1)` 로 사용할 수 있는 이유는 (DB에는 id로 필드 이름이 지정 됨에도) `.get(pk=1)` 이`.get(id__exact=1)` 와 동일한 의미이기 때문

    - 즉, **`pk`는 `id__exact` 의 shortcut** 

      ```python
      >>> Article.objects.get(id__exact=1) # Explicit form
      >>> Article.objects.get(id=1) # __exact is implied
      >>> Article.objects.get(pk=1) # pk implies id__exact
      ```

      

####  3. UPDATE

- DB에 저장된 값을 불러와 수정

  ```python
  >>> article = Article.objects.get(pk=1)
  >>> article.title
  'Title_1'
  
  # 값을 변경하고 저장
  >>> article.title = 'first'
  >>> article.save()
  
  # 정상적으로 변경된 것을 확인
  >>> article.title
  'frist'
  ```

  

####  4. DELETE

- DB에 저장된 값을 불러와 삭제

  ```python
  >>> article = Article.objects.get(pk=1)
  >>> article.delete()
  (1, {'articles.Article': 1})
  
  # 1번 글을 조회하면 해당 객체가 없다고 나옴
  >>> Article.objects.get(pk=1)
  DoesNotExist: Article matching query does not exist.
  ```

  

## 5. Admin Site

> - Automatic Admin Interface
>   -  사용자가 아닌 서버 관리자가 활용하기 위한 페이지
>   - Article class를 `admin.py`에 등록하고 관리
>   - `django.contrib.auth` 모듈에서 제공
>   - record 생성 여부 확인과 CRUD 로직 파악에 매우 유용



####  1. 관리자 생성

- 관리자 계정 생성 👉 서버 실행 👉 `/admin` 페이지 로그인

  ```bash
  $ python manage.py createsuperuser
  ```

  - Username, E-mail, Password 입력

- 모델을 등록하지 않을 경우, 기본적인 사용자 정보만 확인 가능



####  2. Model 등록

- `admin.py`에 Model Class를 등록하여 record 조회

  ```python
  # app_name/admin.py
  
  from django.contrib import admin
  from .models import Model_Name
  
  admin.site.register(Model_Name)
  ```

  - **ModelAdmin options**: `list_display`

    - admin 페이지에 `models.py`에서 정의한 각각의 속성(컬럼)들의 값(레코드) 출력 가능

      ```python
      # app_name/admin.py
      
      from django.contrib import admin
      from .models import Model_Name
      
      class ArticleAdmin(admin.ModelAdmin):
          # 표시할 속성 값 작성
          list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
      
      admin.site.register(Model_Name, ArticleAdmin)
      ```



####  3. Admin Site 확인

- 현재까지 작성한 글 확인 가능
- `admin.py` 는 관리자 사이트에 Article 객체가 관리 인터페이스를 가지고 있다는 것을 알려주는 것
- `models.py` 에 정의한 `__str__` 의 형태로 객체가 표현

