# 08. Django Model Relationship



## 1. 1:N 관계

#### 1. Foreign Key

- RDBMS에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키 👉 외래 키
- 참조하는 테이블에서 1개의 키(속성)에 해당하고, 이는 참조되는 테이블의 PK
- **특징**
  - 키를 사용하여 부모 테이블의 유일한 값을 참조 👉 참조 무결성
  - 외래 키의 값이 반드시 부모 테이블의 PK일 필요는 없지만, 유일해야 함



#### 2. `ForeignKey` field

- 2개의 필수 위치 인자
  - 참조하는 model class
  - `on_delete` 옵션
    - ForeignKey가 참조하는 부모 객체가 삭제될 경우, 해당 데이터 처리 방식 설정
    - 데이터 무결성을 위해 매우 중요한 설정
    - `CASCADE`, `PROTECT`, `SET_NULL`, `SET_DEFAULT` 등



#### 3. Comment

- 1:N 모델 생성

  ```python
  # models.py
  from django.conf import settings
  
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.content
  ```

  - Article : Comment = 1 : N	/ 	User : Comment = 1 : N
  - Django는 개발자가 지정한 필드에 `_id`를 추가하여 데이터베이스 필드 이름을 생성
    - `article_id`와 `user_id` 라는 컬럼이 생성되는 것!



- **1:N 관계 manager**

  - **Article(1)** : **Comment(N)** : `comment_set`
    - `article.comment` 형태로는 가져올 수 없다. 
    - 게시글에 몇 개의 댓글이 있는지 Django ORM이 보장할 수 없기 때문
    - 본질적으로는 Article 클래스에 Comment 와의 어떠한 관계도 연결하지 않음
  - **Comment(N)** : **Article(1)** : `article`
    
- 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로 `comment.article`와 같이 접근할 수 있음
    
- `related_name`
  
  - 부모 테이블에서 역으로 참조할 때(the relation from the related object back to this one.) `모델이름_set` 이라는 형식으로 참조한다. (**역참조**)
  
  - related_name 값은 django 가 기본적으로 만들어 주는 `_set` manager를 임의로 변경할 수 있다.
  
      ```python
      # articles/models.py
      
      class Comment(models.Model):
          article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
        ...
    ```
  
  - 위와 같이 변경하면 `article.comment_set` 은 더이상 사용할 수 없고 `article.comments` 로 대체된다.
  
    - 1:N 관계에서는 거의 사용하지 않지만 M:N 관계에서는 반드시 사용해야 할 경우가 발생한다.





## 2. M:N 관계

#### 1. `ManyToManyField`

- 1개의 필수 인자 👉 관계를 설정할 model class
- **Argument**
  
  - `related_name`
  
  - `symmetrical`
    
    - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
    
      ```python
      from django.db import models
      
      class Person(models.Model):
          friends = models.ManyToManyField('self', symmetrical=False)
      ```
    
      - 예시처럼 동일한 모델을 가리키는 정의의 경우 django는 Person 클래스에 person_set 매니저를 추가하지 않음
      - 대신 대칭적(`symmetrical`)이라고 간주하며, source 인스턴스가 target 인스턴스를 참조하면 target 인스턴스도 source 인스턴스를 참조
      - **BUT!** self와의 관계에서 **대칭을 원하지 않는 경우** `symmetrical=False`로 설정
    
  - `through`
  
    - Django는 다대다 관계를 관리하는 중개 테이블을 자동으로 생성
  
    - 중간 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
  
      👉 일반적으로 추가 데이터를 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용



- **methods**
  - `add()`
    - "지정된 객체를 관련 객체 집합에 추가"
    - 이미 존재하는 관계에 add()를 사용하면 관계가 복제되지 않음
  - `remove()`
    - "관련 객체 집합에서 지정된 모델 개체를 제거"
    - QuerySet.delete()를 사용하여 관계가 삭제됨
  - clear(), set(), create()



- **중개 테이블 필드 생성 규칙**
  1. 소스(source model) 및 대상(target model) 모델이 다른 경우
     - id
     - `<containing_model>_id`
     - `<other_model>_id`
  2. ManyToManyField가 동일한 모델을 가리키는 경우
     - id
     - `from_<model>_id`
     - `to_<model>_id`



#### 2. LIKE

- M:N model 설정

  ```python
  # articles/models.py
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
      ...
  ```

  - **현 상황에서는 `related_name` 작성이 필수**

    - M:N 관계 설정 시에 `related_name` 이 없다면 자동으로 `.article_set` 매니저를 사용할 수 있도록 하는 데 이 매니저는 이미 이전 1:N(User:Article) 관계에서 사용 중인 매니저!

      👉 user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 구분 불가

      👉 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 추가 작성이 필요



- LIKE 기능 구현

  ```python
  # articles/views.py
  
  @require_POST
  def likes(request, article_pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article_pk)
  
          if article.like_users.filter(pk=request.user.pk).exists():
              article.like_users.remove(request.user)
          else:
              article.like_users.add(request.user)
          return redirect('articles:index')
      return redirect('accounts:login')
  ```

  - `exist()`

    - 최소한 하나의 레코드가 존재하는지 여부를 확인 
    - 쿼리셋 cache를 만들지 않으면서 특정 레코드가 존재하는지 검사
      - 결과 전체가 필요하지 않은 경우 유용

  - `index.html` 에 추가

    ```django
    {# articles/index.html #}
    
    {% extends 'base.html' %}
    
    {% block content %}
      ...
      {% for article in articles %}
        ...
        <div>
          <form action="{% url 'articles:likes' article.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in article.like_users.all %}
              <button>좋아요 취소</button>
            {% else %}
              <button>좋아요</button>
            {% endif %}
          </form>
        </div>
        <p>{{ article.like_users.all|length }} 명이 이 글을 좋아합니다.</p>
        ...
    {% endblock %}
    ```



#### 3. Follow

- 자연스러운 Follow 흐름을 위한 프로필 페이지 작성

  ```python
  # accounts/views.py
  def profile(request, username):
      person = get_object_or_404(get_user_model(), username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```



- M:N 관계 설정

  ```python
  # accounts/models.py
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```



- Follow 기능 구현

  ```python
  # accounts/views.py
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          person = get_object_or_404(get_user_model(), pk=user_pk)
          if person != request.user:
              if person.followers.filter(pk=request.user.pk).exists():
                  person.followers.remove(request.user)
              else:
                  person.followers.add(request.user)
          return redirect('accounts:profile', person.username)
      return redirect('accounts:login')
  ```

  ```django
  {# accounts/profile.html #}
  
  <div> 
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <button>Unfollow</button>
          {% else %}
            <button>Follow</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
  ```

  - cf. `with` template tag

    - 더 간단한 이름으로 복잡한 변수를 저장한다.
    - 주로 데이터베이스에 중복으로 여러번 엑세스 할 때 유용하게 사용한다.
    - 변수는 `{% with %}` and `{% endwith %}` 사이에서만 사용 가능하다.

    ```django
    {% with followings=person.followings.all followers=person.followers.all %}
      <div> 
        <div>
          팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
        </div>
        {% if request.user != person %}
          <div>
            <form action="{% url 'accounts:follow' person.pk %}" method="POST">
              {% csrf_token %}
              {% if request.user in followers %}
                <button>Unfollow</button>
              {% else %}
                <button>Follow</button>
              {% endif %}
            </form>
          </div>
        {% endif %}
      </div>
    {% endwith %}
    ```

    

