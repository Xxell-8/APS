# 05. Django Files



## 1. Static Files

- 웹 사이트의 구성 요소 중에 image, css, js 등 해당 내용이 고정되어 응답 시 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일



####  1. Static Files 사용

- `django.contrib.staticfiles`가 등록 확인 (PROJECT 생성 시 자동 등록)

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

- `settings.py`에 `STATIC_URL` 정의

  📌 기본 static 경로는 `app_name/static/`

  ```python
  # settings.py
  
  STATIC_URL = '/static/'
  ```

- Templates에서 `static tag`를 통해 사용

  - 이미지 파일 위치 👉 `articles/static/articles/images/`

  ```django
  {% extends 'base.html' %}
  {% load static %}
  
  {% block content %}
    <img src="{% static 'articles/images/sample.png' %}" alt="sample">
    ...
  {% endblock %}
  ```

  

####  2. `staticfiles` in settings.py

- `STATIC_ROOT`

  - Django PROJECT에서 사용하는 모든 정적 파일을 한 곳에 모아놓는 경로

  - 실제 서비스 **배포 환경에서 필요**한 경로

    - `DEBUG=True`(개발 단계)로 설정되어 있으면 작용하지 않음
    - 개발 단계에서는 경로를 작성하지 않아도 동작

  - collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로

    - `collectstatic`: 배포 시 흩어져 있는 정적 파일을 특정 DIR로 옮기는 작업

    ```python
    # setting.py
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```

    ```bash
    $ python manage.py collectstatic
    ```

  

- `STATIC_URL`

  - `STATIC_ROOT`에 있는 정적파일을 참조 할 때 사용할 URL
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
  - 비어 있지 않은 값으로 설정한다면, 반드시 `/`(slash)로 끝나야 함



- `STATICFILES_DIRS`

  - 기본 경로 외에 추가적인 정적 파일 경로 정의

  ```python
  # settings.py
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'crud' / 'static',
  ]
  ```

  

## 2. Media

- 사용자가 웹에서 업로드하는 정적 파일



####  1. `FileField` / `ImageField` 사용

- `settings.py`에 `MEDIA_ROOT`, `MEDIA_URL` 설정
- `upload_to` 속성을 정의하여 `MEDIA_ROOT`의 하위 경로 지정 가능
- 업로드된 파일의 상대 URL은 django가 제공하는 URL 속성으로 얻을 수 있음



####  2.  `mediafiles` in settings.py

- `MEDIA_ROOT`

  - 사용자가 업로드한 파일을 보관할 디렉토리의 절대 경로
  - 실제 해당 파일의 업로드가 끝나면 어디에 저장할 지 결정
    - cf. 성능을 위해 **DB에는** 파일이 아닌 **파일 경로 저장**
  - `MEDIA_ROOT`는 `STATIC_ROOT`와 다른 경로로 지정을 해야 함

  

- `MEDIA_URL`

  - 업로드된 파일의 URL을 만들어주는 역할
    - 일반 사용자가 사용하는 public URL
  - 비어 있지 않은 값으로 설정하면, 반드시 `/`(slash)로 끝나야 함
  - `MEDIA_URL`도 `STATIC_URL`과 경로가 달라야 함

  ```python
  # settings.py
  MEDIA_ROOT = BASE_DIR / 'media'
  MEDIA_URL = '/media/'
  ```



#### 3. Media Files 제공 설정 (개발 단계)

>  개발 단계에서는 `django.views.static.serve()` view를 사용하여 MEDIA_ROOT에서 사용자가 업로드한 미디어 파일 제공

- `urls.py` 설정

  - 미디어 파일의 URL: `settings.MEDIA_URL`
  - URL을 통해 참조하는 파일의 실제 위치: `settings.MEDIA_ROOT`

  ```python
  # PROJECT/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  

- CRUD 적용

  - `models.py` 수정 

    ```python
    class Article(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField()
        image = models.ImageField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

    - 기존 모델에 추가할 경우, 코드 순서와 관계 없이 실제 테이블에서는 가장 우측(맨 뒤)에 추가

      ```bash
      $ pip install Pillow
      
      # 모델 수정 후 migration
      $ python manage.py makemigrations
      $ python manage.py migrate
      ```

    - `blank` (model field option)

      - `blank=True`일 경우, 해당 field는 빈 값을 허용
      - DB에는 `''`(빈 문자열) 저장

  

  - `FileField` / `ImageField` 사용할 경우

    - `templates` 설정

      - MEDIA의 변수명과 변수 속성 활용

        ```django
        {% extends 'base.html' %}
        
        {% block content %}
          <h2 class='text-center'>DETAIL</h2>
          <h3>{{ article.pk }} 번 글</h3>
          <img src="{{ article.image.url }}" alt="{{ article.image }}">
          <hr>
          ...
        {% endblock %}
        ```

        - `article.image.url` 👉 업로드 파일의 상대 URL
        - `article.image` 👉 업로드 파일의 파일 이름

        

      - `form` tag에 `enctype="multipart/form-data"` 추가

        ```django
        <form action="" method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
        </form>
        ```

      - [참고] `enctype` 속성 (in form tag)

        ① `apllication/x-www-form-urlencoded`

        - (기본값) 모든 문자 인코딩

        ② `multipart/form-data`

        - 파일/이미지 업로드 시에 반드시 사용 (전송되는 데이터의 형식을 지정)
        - `<input type="file">`을 사용할 경우 사용

        ③ `text/plain`

      - [참고] `accept` 속성 (in input tag)

        - 입력 허용할 파일 유형을 나타내는 문자열
        - 이 문자열은 쉼표로 구분된 고유 파일 유형 지정자(unique file type specifiers)
        - 하지만 파일 검증은 하지 못함 (이미지만 accept 해 놓더라도 비디오나 오디오 파일을 제출할 수 있음)

        

    - `view.py` 설정

      - `ModelForm` 사용 시, `files` 속성 추가

        ```python
        @require_http_methods(['GET', 'POST'])
        def view_name(request):
            if request.method == 'POST':
                # form = ArticleForm(data=request.POST, files=request.FILES)
                # ModelForm의 인자의 순서가 data, files로 시작해서 키워드 생략 가능
                form = ArticleForm(request.POST, request.FILES)
                ...
        ```

        

