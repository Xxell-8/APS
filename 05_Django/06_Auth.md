# 06. Django Auth



## 1. INTO 

#### 1. Authentication System

> - Authentication System in Django
>   - 인증과 권한 부여가 어느 정도 결합되어 있으며, 이를 함께 제공
>   - 인증과 관련한 Built-in forms 제공
>     - 회원가입(`UserCreationForm`), 로그인(`Authentication Form`) 등



- **Authentication** (인증)
  - 자신이 누구하고 주장하는 사람의 **신원을 확인**
- **Authorization** (권한 , 허가)
  - 가고 싶은 곳으로 가도록 혹은 **원하는 정보를 얻도록 허용하는 과정**



#### 2. HTTP

- Hyper Text Transfer Protocol
  - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초



##### 🚩 HTTP의 특징 👉 보완을 위해 Cookie & Session 등장

- **비연결지향(connectionless)**
  - 서버는 응답 후 접속을 끊음
- **무상태(stateless)**
  - 접속이 끊어지면 클라이언트와 서버간의 통신이 끝나며,
  - 상태를 저장하지 않음



#### 3. Cookie

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 브라우저(클라이언트)는 전송받은 쿠키를 로컬에 `key-value`의 데이터 형식으로 저장
  
- **동일한 서버에 재요청 시** 저장된 쿠키를 함께 전송
  
- 사용 목적

  - **세션 관리**

    - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

  - 개인화

    - 사용자 선호, 테마 등의 세팅

  - 트래킹

    - 사용자 행동을 기록 및 분석하는 용도

    

- **cf. Cookie lifetime**

  - **Session cookie**
    - 현재 세션이 종료되면 삭제
    - 브라우저는 현재 세션이 종료되는 시기를 정의
    - 일부 부라우저는 다시 시작할 때 세션 복원을 사용해 계속 지속될 수 있도록 함
  - **Permanent cookie**
    - `Expires` 속성에 지정된 날짜 혹은 `Max-Age` 속성에 지정된 기간이 지나면 삭제



#### 4. Session

- 사이트와 특정 브라우저 사이의 **`state(상태)`를 유지**시키는 것

  👉 HTTP의 특징을 보완

  👉 주로 로그인 상태 유지 등에 사용

- 클라이언트가 서버에 접속하면 서버가 특정 **session id를 발급**

  - 클라이언트는 **session id를 쿠키를 사용해 저장**
    - 재접속 시, 해당 쿠키를 이용해 서버에 **session id 전달**

- Session in Django

  - Django는 특정 session id를 포함하는 쿠키를 사용해 각각의 브라우저와 사이트가 연결된 세션을 파악
    - 세션 정보는 DB의 `django_sessions` 테이블에 저장



#### 🚩 Cookie & Session

- Cookie : 클라이언트 로컬에 파일로 저장

- Session : 서버에 저장

  - 서버에 저장된 세션 데이터를 구별하기 위한 session id는 쿠키로 로컬에 저장

  #### 👉 **" HTTP 쿠키는 상태가 있는 세션을 만들도록 해준다 "**



## 2. Authentication in Web requests

> - Web Requests
>   - Django는 세션과 미들웨어를 사용하여 인증 시스템을 request 객체에 연결
>   - **사용자를 나타내는 모든 요청에 `request.user` 제공**
>     - 현재 사용자가 로그인하지 않는 경우, `AnonymousUser` 클래스의 인스턴스로 설정
>     - 로그인한 사용자의 경우, `User` 클래스의 인스턴스로 설정
>



#### 1. Accounts

- auth 관련 기능을 담은 APP을 생성할 경우,

  - 반드시 APP_NAME이 `accounts`일 필요는 없지만

  - **auth 관련 기본 설정들이 accounts로 내부적으로 사용**되고 있기 때문에

    - `accounts` 사용 권장

      ```bash
      $ python manage.py startapp accounts
      ```



#### 2. Login

- Session을 `CREATE`하는 로직

  ```python
  # views.py
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm
  
  
  @require_http_methods(['GET', 'POST'])
  def login(request):
      # 로그인 사용자에 대한 접근 제한
      if request.user.is_authenticated:
          return redirect('articles:index')
      
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('accounts:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  ```

  - `login()`

    - 현재 세션에 연결하려는 인증된 사용자가 있는 경우 `login()` 함수로 로그인 진행

    - `HttpRequest` 객체와 `User` 객체를 통해 로그인 진행

      👉 `auth_login(request, form.get_user())`

      📌 cf. view 함수 `login`과의 이름 충돌을 방지하기 위해 `auth_login`으로 사용

    - Django의 session framework를 통해 사용자 ID를 세션에 저장

    

  - `AuthenticationForm`

    - Built-in Form 중 하나이며, **`forms.Form`을 상속**
      - `AuthenticationForm(request, request.POST)`
      - 첫 번째 인자로 **request**, 그 이후에 **data**



#### 3. Logout

- Session을 `DELETE`하는 로직

  ```python
  # views.py
  from django.contrib.auth import logout as auth_logout
  
  @require_POST
  def logout(request):
      # 로그인 사용자에 대한 접근
      if request.user.is_authenticated:
          auth_logout(request)
      return redirect('accounts:index')
  ```

  - `logout()`
    - `HttpRequest` 객체를 받으며, return 값은 없음
    - 현재 요청에 대한 **DB의 세션 데이터를 삭제**하고, **클라이언트 쿠키에서도 `session id`를 삭제**
      - 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 접근하는 것을 방지하기 위한 것



#### 🚩 로그인 사용자에 대한 접근 제한

- **`.is_authenticated`**

  - 사용자가 인증되었는지 확인하는 방법
  - User model의 `속성(attribute)`
    - User에 항상 `True`이며, AnonymousUser에 대해서만 항상 `False`

  📌 이것은 권한(permission)과는 관련이 없으며, 

  📌 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지 확인하지 않음

  

- **`@login_required`** 

  - 사용자가 로그인 했는지 확인하는 **view를 위한 decorator**

    - 로그인된 사용자의 경우, 해당 view 함수 실행

    - 비로그인 사용자의 경우, `settings.LOGIN_URL`에 설정된 절대 경로로 redirect

      - LOGIN_URL의 기본값은 `/accounts/login/`

      - 로그인에 성공하면, redirect할 경로를`next` 쿼리에 저장

        - (로그인 후 접근할 수 있는) 원래 요청했던 주소로 보내기 위해 **keep**해두는 것

        ```python
        # next parameter 활용
        return redirect(request.GET.get('next') or 'accounts:index')
        ```

  - `@login_required` & `@require_POST`

    - 데코레이터 간의 로직상 문제가 발생 가능
      - `@require_POST`를 사용하는 함수에서 `@login_required`를 설정할 경우,
        - 비로그인 상태에서 해당 요청에 접근하면, LOGIN_URL로 연결되고
          - 로그인 후, `next` 매개변수를 따라 해당 함수로 redirect(`GET`)되는데
          - `@require_POST`로 인해 `405 Method Not Allowed` 오류 발생
        - WHY?
          - redirect 중 POST 데이터 손실 발생
          - redirect는 POST 요청이 불가능 👉 GET 요청으로 변경
    - 즉, `@require_POST`를 사용하는 view 함수에서 로그인 인증이 필요할 경우,
      - 함수 내부에서 `.is_authenticated`를 활용



#### 4. 회원가입

- `UserCreationForm` 활용

  -  username과 password로 권한이 없는 user를 create하는 Modelform

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import UserCreationForm
  
  
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```



#### 5. 회원 탈퇴

- 회원 탈퇴는 DB에서 user를 delete

  ```python
  # accounts/views.py
  
  @require_POST
  def delete(request):
      if request.user.is_authenticated:
          request.user.delete()
      return redirect('articles:index')
  ```



#### 6. 회원 수정

- `UserChangeForm`

  - user의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 modelform
  - `forms.py`에서 사용할 필드만 설정해 사용

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  
  
  class CustomUserChangeForm(UserChangeForm):
  
      class Meta:
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
          
  # accounts/views.py
  from .forms import CustomUserChangeForm
  
  
  @login_required
  def update(request):
      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  ```



#### 7. 비밀번호 변경

- `PasswordChangeForm`

  - 비밀번호를 변경할 수 있도록 하는 Form

- `UserChangeForm` 에도 password 필드가 존재하지만 수정은 불가

  - 하단에 '**다만 이 <u>양식</u>으로 비밀번호를 변경할 수 없습니다.**' 라는 문구가 있는데, 이 링크를 클릭하면 `accounts/password/` 라는 주소로 이동

    👉 Django가 기본적으로 설정하고 있는 주소

    👉 해당 URL 활용해서 비밀번호 변경 기능을 구현

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import PasswordChangeForm
  from django.contrib.auth import update_session_auth_hash
  
  
  @login_required
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
    return render(request, 'accounts/change_password.html', context)
  ```

  🚩 **update_session_auth_hash()**

  - 암호 변경 시 세션 무효화 방지
    - 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
    - 현재 요청(current request)과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져와서 session hash를 적절하게 업데이트해 로그아웃을 방지



## 3. Custom Authentication

#### 1. User

- User Objects
  - django 인증 시스템의 핵심
  - 오직 하나의 User Class만 존재
  - 상속 관계
    - `models.Model` 👉 `AbstractBaseUser` 👉 `AbstractUser`  👉 User
  - **`AbstractUser`**
    - User model을 구현하는 완전한 기능을 갖춘 기본 클래스

- User 참조
  - `get_user_model()` method

    - `User`를 직접 참조하는 대신`django.contrib.auth.get_user_model()` 을 사용하여 User model 을 참조해야 한다고 권장

      - **현재 활성화(active)된 user model을 리턴**
      - 커스텀한 유저 모델이 있을 경우는 커스텀 유저 모델, 그렇지 않으면 User를 참조

    - `models.py`가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

    - `models.py`에서 User를 참조할 때는 `settings.AUTH_USER_MODEL` 활용

      ```python
      # models.py 👉 활용 예시
      from django.conf import settings
      
      
      class Article(models.Model):
          user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      ```

      

#### 2. User model 대체하기

- Django는 custom model을 참조하는 `AUTH_USER_MODEL` 설정을 제공하여 default user model을 재정의(override)

- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력하게 권장(highly recommended)

  - 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하지만 필요한 경우 나중에 맞춤 설정할 수 있기 때문

- **프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 대체해야 함!!**

  ```python
  # settings.py
  AUTH_USER_MODEL = 'accounts.User' 
  
  # accounts/models.py
  from django.contrib.auth.models import AbstractUser
  
  
  class User(AbstractUser):
      pass
  
  # accounts/admin.py
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  
  admin.site.register(User, UserAdmin)
  ```

  - **AUTH_USER_MODEL**
    - User를 나타내는데 사용하는 모델
      - 프로젝트를 진행하는 동안 (즉, 프로젝트에 의존하는 모델을 만들고 마이그레이션 한 후) 설정은 변경할 수 없다. (변경하려면 큰 노력이 필요)
      - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함



#### 3. Custom User + Built-in auth forms

- 유저모델 대체 후 회원가입 시 에러 발생

- `AbstractBaseUser`의 모든 subclass와 호환되는 forms

  - `AuthenticationForm`, `SetPasswordForm`, `PasswordChangeForm`, `AdminPasswordChangeForm`

- User와 연결되어 있어서 **커스텀 유저 모델을 사용하려면 다시 작성하거나 확장**해야 하는 forms

  - `UserCreationForm`, `UserChangeForm`

  - `UserCreationForm()` 재정의

    ```python
    # accounts/forms.py
    
    from django.contrib.auth.forms import UserChangeForm, UserCreationForm
    
    
    class CustomUserCreationForm(UserCreationForm):
    
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            fields = UserCreationForm.Meta.fields
    ```

    

