# 04. Django Form

> - Form은 Django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 우연한 데이터 손상에 대한 중요한 방어수단
>
> - Django는 Form에 관련된 작업의 아래 세 부분을 처리
>
>   ① 렌더링을 위한 데이터 준비 및 재구성
>
>   ② 데이터에 대한 HTML forms 생성
>
>   ③ 클라이언트로부터 받은 데이터 수신 및 처리



## 1. Form Class

- Django form 관리 시스템의 핵심
- form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field와 관련한 **에러 메시지 결정**



####  1. Form Class 작성

- [[참고] Form 활용하기](https://docs.djangoproject.com/en/3.1/topics/forms/)

- `articles/forms.py` 생성

  ```python
  # articles/forms.py
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
  ```

  - Form을 작성하면, `views.py`와 `templates` 간소화 가능

    ```python
    # articles/views.py
    from .forms import ArticleForm
      
      
    def new(request):
        # Form Class를 context로 HTML에 전달
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```

    ```django
    {# new.html #}
    {% extends 'base.html' %}
      
    {% block content %}
        <h1>NEW</h1>
        <form action="{% url 'articles:create' %}" method="POST">
            {% csrf_token %}
            {# form을 변수로 사용 #}
            {{ form.as_p }}
            <input type="submit">
        </form>
        <hr>
        <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock %}
    ```

    - Outputting forms as HTML
      - `as_p` : 각 필드가 단락(paragraph)으로 렌더링
      - `as_ul` : 각 필드가 목록 항목(list item)으로 렌더링
      - `as_table` : 각 필드가 테이블 행으로 렌더링
    - Django의 HTML input 요소 표현
      - Form fields
        - 입력에 대한 유효성 검사 로직을 처리
        - Templates에서 직접 사용
      - Widgets
        - 웹 페이지 상에 input 요소 렌더링
        - 제출된 데이터 추출 처리
        - ⚠반드시⚠ form fields에 할당



####  2. Form fields

> - [[참고] Form Fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields)
> - [[참고] Widgets](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/)
> - [[참고] Validators](https://docs.djangoproject.com/en/3.1/ref/validators/)

- Form fields Coding style

  ```python
  class ArticleForm(forms.Form):
      REGION_A = '01'
      REGION_B = '02'
      REGION_C = '03'
      REGION_D = '04'
      # 각 선택지를 묶어 튜플 리스트로 할당
      REGIONS_CHOICES = [
          # (DB에 저장되는 정보, 웹 페이지에 표시될 정보)
          (REGION_A, '서울'),
          (REGION_B, '경기'),
          (REGION_C, '강원'),
          (REGION_D, '제주'),
      ]
      
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
      # ChoiceField 활용 > 그 중 RadioSelect 사용
      region = forms.ChoiceField(
          choices=REGIONS_CHOICES,
          widget=forms.RadioSelect()
      )
  ```

  

## 2. ModelForm

- model을 통해 Form Class를 만들 수 있는 Helper

  - ModelForm 클래스를 사용하여 모델에서 form을 작성
  - 일반 Form과 완전히 같은 방식(객체 생성)으로 view에서 사용

- Meta Class

  - Model 정보를 작성하는 곳
  - 해당 model에 정의한 field 정보를 Form에 적용

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Article
  
  # class ArticleForm(forms.Form):
  #     title = forms.CharField(max_length=10)
  #     content = forms.CharField(widget=forms.Textarea)
  
  class ArticleForm(forms.ModelForm):
      
      class Meta:
          # 모델 등록
          model = Article
          # field 전체 가져오기
          fields = '__all__'
          
          # cf. 사용할 field만 가져오려면, 튜플로 작성 
          # fields = ('title', 'content',)
          # cf. 특정 field를 제외
          # exclude = ('title',)
  ```



- `Form` vs `ModelForm`
  - Form
    - 어떤 model에 저장해야 하는지 알 수 없으므로,
      - 유효성 검사 이후 `cleaned_data` 딕셔너리 생성
      - cleaned_data 딕셔너리에서 `.get`으로 데이터를 가져온 후,
        -  `article = Article(title=title, content=content)` 를 사용해서  `.save()` 호출
    - **model에 연관되지 않은 데이터**를 받을 때 사용
  - ModelForm
    - Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
    - 어떤 레코드를 만들어야 하는지 알고 있으므로 바로 `.save()` 호출 가능



- `Widgets`

  - Django의 HTML input 요소 표현

  ```python
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title', 
                  'placeholder': 'Enter the title',
                  'maxlength': 10,
              }
          ),
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content',
                  'placeholder': 'Enter the content',
                  'rows': 5,
                  'cols': 50,
              }
          ),
          error_messages={
              'required': 'Please enter your content',
          }
      )
      
      class Meta:
          model = Article
          fields = '__all__'
  ```



## 3. Change view structure (feat. ModelForm)

####  1. CREATE

- `new` + `create`

  ```python
  # articles/views.py
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```



####  2. UPDATE

- `edit` + `update`

  - 기존 데이터를 가져와 수정하는데,
    - `instance`를 통해 수정 대상이 되는 객체를 지정

  ```python
  # articles/views.py
  
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'form': form,
          'article': article,
      }
      return render(request, 'articles/update.html', context)
  ```

  

## 4. Form in Django HTML

> - form을 커스텀하는 다양한 방법



####  1. 직접 form 작성

- Rendering fields manually

  ```django
  ...
  {# action을 비워두면 현재 페이지로 요청 #}
  <form action="" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <button class="btn btn-primary">작성</button>
  </form>
  ```

- Looping over the form's fields 👉 `{{% for %}}`

  ```django
  ...
  <form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
        {{ field.errors }}
        {{ field.label_tag }}
        {{ field }}
    {% endfor %}
    <button class="btn btn-primary">작성</button>
  </form>
  ```



####  2. Bootstrap Form

- `class` 설정 👉 `form-control`

  ```django
  <form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
      <div class="mb-3">
        {{ field.errors }}
        {{ field.label_tag }} 
        {{ field }}
      </div>
    {% endfor %}
    <button class="btn btn-primary">작성</button>
  </form>
  ```

  ```python
  # articles/forms.py
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          label='제목',
          widget=forms.TextInput(
              attrs={
                  # form-control 추가
                  'class': 'my-title form-control', 
                  'placeholder': 'Enter the title',
          }),
      )
      ...
  ```

- **Error message** with Bootstrap

  ```django
  <form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
      {% if field.errors %}
        {% for error in field.errors %}
      	{# 에러메시지를 alert로 표시 #}
          <div class="alert alert-warning" role="alert">{{ error|escape }}</div>
        {% endfor %}
      {% endif %}
      <div class="form-group">
        {{ field.label_tag }} 
        {{ field }}
      </div>
    {% endfor %}
    <button class="btn btn-primary">작성</button>
  </form>
  ```



#### 3. Django-bootstrap5

- [[참고] bootstrap5 Docs](https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html)

- 설치 및 등록

  ```bash
  $ pip install django-bootstrap-v5
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
    ...
    'bootstrap5',
     ...
  ]
  ```

- `base.html` 수정

  ```django
  {# bootstrap5 사용을 위해 load #}
  {% load bootstrap5 %}
  
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    ...
    {% bootstrap_css %}
    <title>Document</title>
  </head>
  <body>
    ...
    {% bootstrap_javascript %}
  </body>
  </html>
  ```

- `bootstrap_form` 활용

  ```django
  {% extends 'base.html' %}
  {% load bootstrap5 %}
  
  {% block content %}
    ...
    <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form layout='horizontal' %}
      {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
    </form>
    ...
  {% endblock %}
  ```



## 5. View decorator

- Decorator

  - 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 `연장`하게 해주는 `함수`
  - Django는 다양한 HTTP 기능을 지원하기 위해 view에 적용 할 수있는 여러 데코레이터를 제공

- Allowed HTTP methods

  - request method에 따라 view 함수에 대한 접근을 제한
  - 요청이 조건을 충족하지 못하면,
    -  `405 Method Not Allowed` 에러 발생

  ```python
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  ```



1. `require_http_methods()`

   - view가 특정 request method만 허용

     ```python
     @require_http_methods(['GET', 'POST'])
     def create(request):
         pass
     ```

2. `require_POST()`

   - view가 POST method만 허용

     ```python
     @require_POST
     def delete(request, pk):
         article = Article.objects.get(pk=pk)
         article.delete()
         return redirect('articles:index')
     ```

3. `require_safe()`

   - view가 GET method만 허용

   - `require_GET()`도 존재하나, `require_safe` 사용

     ```python
     @require_safe
     def index(request):
         pass
     ```

     