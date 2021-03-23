# [참고] Djnago Project etc.

 

## 1. 가상환경

- 파이썬 인터프리터, 라이브러리 및 스크립트가 '시스템 파이썬' (즉, 운영 체제 일부로 설치되어 있는 것)에 설치된 모든 라이브러리와 격리되어 있는 파이썬 환경
- 각 가상 환경(복제본)은 고유한 파이썬 환경을 가지며 독립적으로 설치된 패키지 집합을 가짐
- 대표적인 가상 환경 지원 시스템
  - venv, virtualenv, conda, pyenv
  - 파이썬 3.3 부터 venv가 기본 모듈로 내장

- **WHY?**
  - pip로 설치한 패키지들은 Lib/site-packages 안에 저장되는데, 이는 모든 파이썬 스크립트에서 사용할 수 있음
    - 여러 프로젝트를 진행할 경우, 프로젝트마다 다른 버전의 라이브러리가 필요할 수도 있는데 파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능
    - 각 라이브러리나 모듈은 서로에 대한 의존성이 다르기 때문에 알 수 없는 충돌이나 기타 문제가 발생
  - 즉, 프로젝트마다 가상 환경을 구성하여 라이브러리, 모듈 등을 따로 관리



#### Django Project 적용

1. 가상환경 구성

   ```bash
   $ python -m venv venv
   ```

2. Python Interpreter 👉 `venv` 설정 후  Terminal ON

3. 필요한 라이브러리 설치 👉 `requirements.txt` 생성

   ```bash
   $ pip install ~
   $ pip freeze > requirements.txt
   ```

   - requirements에 있는 라이브러리를 설치해야 할 경우

     ```bash
     $ pip install -r requirements.txt
     ```

4. Django Project 진행



## 2. `get_object_or_404`

- `pk(int)`를 사용하는 기능(detail·update·delete)은 기존의 `get` 방식을 사용해 record를 가져올 경우,

  - 사용자가 존재하지 않는 pk를 입력했을 때,

    - `500 Internal Server error`를 표시

      👉 즉, 서버 측의 오류로 나타나며, 내부 코드가 보일 수 있음

  - **`get_object_or_404()` 활용**하면, 

    - 존재하지 않는 pk 입력 시 `404` 에러를 표시

  ```python
  from django.shortcuts import get_object_or_404
  
  def view_name(request, pk):
      # article = Article.objects.get(pk=pk)
      article = get_object_or_404(Article, pk=pk)
  ```

  

## 3. `django-imagekit`

- 사용자가 업로드한 image 파일의 크기, 해상도 등을 조정할 수 있는 외부 라이브러리

- [[참고] django-imagekit Docs](https://pypi.org/project/django-imagekit/)

- imagekit 활용

  - `Pillow`가 설치되어 있는지 확인

  - `imagekit` 설치 및 등록

    ```bash
    $ pip install django-imagekit
    ```

    ```python
    INSTALLED_APPS = [
        ...,
        'imagekit',
        ...,
    ]
    ```

  - `models.py` 설정

    ```python
    from django.db import models
    from imagekit.models import ImageSpecField
    from imagekit.models import ProcessedImageField
    from imagekit.processors import ResizeToFill
    
    # Create your models here.
    class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        
        # image = models.ImageField(blank=True)
        # image_thumbnail = ImageSpecField(source='image',
        #                                   processors=[ResizeToFill(200, 200)],
        #                                   format='JPEG',
        #                                   options={'quality': 60})
        
        image = ProcessedImageField(upload_to='images/%Y/%m/%d/',
                                               processors=[ResizeToFill(500, 500)],
                                               format='JPEG',
                                               options={'quality': 100})
    
        created_at = models.DateTimeField(auto_now_add=True)
    ```

    

## 4. etc.

- **TIP** for `templates` 유지 보수
  - navbar, card 등 코드가 길어질 수 있는 components는 따로 빼서 HTML 파일로 작성
    - component 파일인 걸 쉽게 확인할 수 있도록 `_name.html`로 저장
  - `{% include "_name.html" %}` 로 원하는 위치에 포함