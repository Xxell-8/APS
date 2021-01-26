# 07. Module

> 파일 단위의 코드 재사용 ☝
>
> - 모듈(Module)
> - 패키지(Package)



## 1. 개념 정리

1. 모듈(Module)

   - 특정 기능을 `.py` 파일 단위로 작성

2. 패키지(Package)

   - 특정 기능과 관련된 여러 모듈의 집합
   - 패키지 안에는 또 다른 서브 패키지를 포함할 수 있음

3. 파이썬 표준 라이브러리

   - PSL, Python Standard Library

   - 파이썬에 기본적으로 설치된 모듈과 내장 함수

4. 패키지 관리자(`pip`)

   - `PyPI`에 저장된 외부 패키지들을 설치하도록 도와주는 패키지



## 2. Module

- 모듈을 활용하기 위해 반드시 `import` 문을 통해 해당 스코프의 지역 이름 공간에 이름이나 이름들을 정의

  ```python
  import module
  from module import var, function, Class
  from module import *
  ```

  

- 모듈 내의 함수를 자주 사용한다면, 변수에 할당해서 사용 가능

  ```python
  import math
  
  sqrt = math.sqrt
  list(map(sqrt, range(1, 6)))
  ```

  

## 3. Package

- 패키지는 `.`(점)으로 구분된 모듈 이름(package.module)을 써서 모듈을 구조화하는 방법

- `from`과 `import` 키워드를 통해  코드를 가져와 활용

  ```python
  from package import module
  from package.module import var, function, Class
  ```

  

  - (example) 아래와 같은 패키지가 있을 때,

    ```
    my_cat/
        __init__.py
        pepper/
            __init__.py
            tools.py # func: plus, minus
        kanda/
            __init__.py
            tools.py # func: mul, div
    ```

  - 패키지 활용

    ```python
    # my_cat의 pepper 사용
    from my_cat import pepper
    
    # my_cat의 pepper의 tools 모듈 사용
    from my_cat.pepper import tools
    
    # my_cat의 pepper의 tools의 plus 함수 사용
    from my_cat.pepper.tools import plus
    ```



- `__init__.py`
  - python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식
  - BUT, 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것을 권장

- `__name__`
  - 모듈의 이름이 저장되는 변수
  - 파이썬 인터프리터로 스크립트 파일을 **직접 실행**할 때는 모듈의 이름이 아니라 `__main__`이 들어간다
  - 해당 파일을 다른 파일에서 **import해서 사용**하면 파일 이름으로 정해진다



