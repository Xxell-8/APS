# 03. Djnago CRUD



## 1. INTRO

 ####  1. 기본 설정

- STEP 1. PROJECT 생성 👉 APP 생성 및 등록 

  ```bash
  $ django-admin startproject crud .
  $ python manage.py runserver # 확인 후 종료
  $ python manage.py startapp articles
  ```

  ```python
  # crud/settings.py
  
  INSTALLED_APPS = [
      'articles',
      ...
  ]
  ```

  

- STEP 2. `templates` & `urls.py` 분리

  - `crud/templates` 폴더 생성

    👉 PROJECT 템플릿 경로 추가

    ```python
    # crud/settings.py
    TEMPLATES = [
        {
            ...,
            'DIRS': [BASE_DIR / 'crud' / 'templates',],
    		...,
        }
    ]
    ```

    👉 `base.html` 설정

    ```django
    <!-- crud/templates/base.html -->
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <!-- Bootstrap CDN -->
    </head>
    <body>
      <div class="container">
        {% block content %}
        {% endblock %}
      </div>
      <!-- Bootstrap CDN -->
    </body>
    </html>
    ```

  - `crud/urls.py` 설정

    ```python
    # crud/urls.py
    
    from django.contrib import admin
    from django.urls import path, include
    
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ]
    ```

    - `articles/urls.py` 분리



####  2. HTTP `POST` method 

- 글을 작성하거나 데이터를 서버로 보낼 때, `GET`이 아닌 `POST` 요청을 사용

  - **WHY?**

    ① HTML 파일을 요청하는 `GET`이 아니라 **record를 생성하는 요청**이기 때문에 `POST`를 사용

    ② **데이터는 URL에 직접 노출되면 안됨**

    ​	👉 Query의 형태를 통해 DB 스키마 유추 가능

    ​	📌 `GET` 요청은 URL을 통해 접근하기 때문에 `POST` 사용

    ③ DB를 조작하고 서버에 변경사항을 만드는 요청일 경우, **최소한의 신원 확인과 검증이 필요**

    

- `GET`과 `POST`의 차이

  - `GET`

    - 특정 리소스를 가져오도록 요청할 때 사용

      👉 반드시 데이터를 가져올 때만 사용해야 함

    - DB에서 데이터를 가져오는 READ의 역할을 수행하며, DB에 변화를 주지 않음

      👉 누가 요청을 보내든 정보를 조회(get HTML)하는 것이기 때문에 문제가 되지 않음

  - `POST`

    - 서버로 데이터를 전송할 때 사용

    - CRUD 중 C·U·D의 역할을 하며 **서버에 변경사항**을 만드는데,

      - DB를 조작하는 요청이기 때문에 요청자에 대한 최소한의 검증이 없으면, 부작용 발생
        - 아무나 DB에 접근해서 데이터를 조작할 수 있게 되는 것

      👉 **`csrf_token`**을 통해 요청자의 신원 확인이 필요

      

- **CSRF Token**

  - Cross-Site-Request-Forgery (사이트 간 요청 위조)

    - 웹 애플리케이션 취약점 중 하나로 **사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법**을 의미
    - `{% csrf_token %}` 을 설정하면 input type hidden 으로 특정한 hash 값이 포함

  - `{% csrf_token %}` 이 없으면, `403 forbidden` 에러 발생

    - 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환하는 HTTP 오류 코드

    - 서버 자체 또는 서버에 있는 파일에 접근할 권한이 없을 경우에 발생

      - 이러한 접근을 할 수 있도록 하는 것이 `{% csrf_token %}` 

        ex. 사내 인트라넷 서버를 사내가 아닌 밖에서 접속하려고 할 때도 해당 HTTP 응답 코드 반환



####  3. Redirect()

- `POST` 요청은 HTML 문서를 렌더링 하는 것이 아니라 데이터 처리를 요청하는 것이기 때문에
  - 처리 후 결과를 볼 수 있는 페이지로 바로 넘겨주는 것이 일반적
- POST 요청은 데이터를 HTTP body에 담아 전송하기 때문에
  - 데이터는 URL에 표시되지 않음
  - 요청 처리 후 HTML 파일을 받아볼 수 있는 곳으로 `redirect `



## 2. READ

#### 1. 게시글 전체 조회

- `index`

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  
  # articles/views.py
  def index(request):
      articles = Article.objects.all()
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```

  ```django
  {# articles/templates/articles/index.html #}
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Articles</h1>
    <hr>
    {% for article in articles %}
      <p>글 번호: {{ article.pk }}</p>
      <p>글 제목: {{ article.title }}</p>
      <p>글 내용: {{ article.content }}</p>
      <hr>
    {% endfor %}
  {% endblock %}
  ```

  - 게시글 정렬 순서 변경 (최신순, pk 내림차순)

    ```python
    # articles/views.py
    
    def index(request):
        # 1. python 조작
        articles = Article.objects.all()[::-1]
        # 2. DB 조작
        articles = Artile.objects.order_by('-pk')  
    ```

    

#### 2. 게시글 상세 조회

- `detail`

  - Variable Routing을 활용해 `pk` 값으로 해당 게시글 상세 조회 가능

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('<int:pk>/', views.detial, name='detail'),
  ]
  
  # articles/view.py
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```django
  {# articles/templates/articles/detail.html #}
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    <hr>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성 시각: {{ article.created_at }}</p>
    <p>수정 시각: {{ article.updated_at }}</p>
    <hr>
    {# edit & delete 추가 #}
    <a href="{% url 'articles:edit' article.pk %}" class="btn btn-warning">EDIT</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-danger">DELETE</button>
    </form>
  
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock %}
  ```

  

## 3. CREATE

- `new`

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('new/', views.new, name='new'),
  ]
  
  # articles/views.py
  def new(request):
      return render(request, 'articles/new.html')
  ```

  ```django
  {# templates/articles/new.html #}
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
      <label for="title">Title: </label>
      <input type="text" name="title"><br>
      <label for="content">Content: </label>
      <textarea name="content" cols="30" rows="5"></textarea><br>
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock %}
  ```



- `create`

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('create/', views.create, name='create'),
  ]
  
  # articles/views.py
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
      
      article = Article(title=title, content=content)
      article.save()
      
      # return render(request, 'articles/create.html')
      # 게시글 생성 후 해당 상세 페이지로 연결
      return redirect('articles:detail', article.pk)
  ```

  ```django
  {# templates/articles/create.html #}
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>성공적으로 글이 작성되었습니다.</h1>
  {% endblock %}
  ```

  

## 4. UPDATE

- `edit`

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('<int:pk>/edit/', views.edit, name='edit'),
  ]
  
  # articles/views.py
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/edit.html', context)
  ```

  ```django
  {# templates/articles/edit.html #}
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
      {% csrf_token %}
      <label for="title">Title: </label>
      <input type="text" name="title" value="{{ article.title }}"><br>
      <label for="content">Content: </label>
      <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea><br>
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock %}
  ```

  

- `update`

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('<int:pk>/update/', views.update, name='update'),
  ]
  
  # articles/views.py
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      article.title = request.POST.get('title')
      article.content = request.POST.get('content')
      article.save()
      return redirect('articles:detail', article.pk)
  ```



## 5. DELETE

- `delete`

  ```python
  # articles/urls.py
  urlpatterns = [
      ...,
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  
  # articles/views.py
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      return redirect('articles:detail', article.pk)
  ```
  


