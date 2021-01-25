# 04. Function

> 함수는 특정한 기능을 하는 코드의 묶음



## 1. def

* 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 그 아래  `들여쓰기`로 코드 블록을 작성


* 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. 


  * `return` 값이 없으면, `None`을 반환

  - ```python
    def <함수 이름>(parameter1, parameter2):
        <코드 블럭>
        return <결과 값>
    ```

- `print()` vs `return`
  - `print()` 함수는 None을 반환 👉 출력값 저장(할당) 불가
  - `return`은 값 자체를 반환



## 2. Output

- 함수의 `return` 값은 **오직 한 개의 객체**만 가능
  - `,`로 이어서 여러 개를 return하면 `tuple`로 반환
- 함수는 `return`을 만나면 종료



## 3. Input

- 매개변수(parameter)는 입력을 받아 함수 내부에서 활용할 `변수`
- 전달인자(argument)는 실제로 전달되는 `입력값` 

##### # 함수의 인자

1. 위치 인자(Positional Arguments)

   - 함수는 기본적으로 인자를 위치로 판단

   

2. 기본 인자 값(Default Argument Values)

   - 함수 호출시, 인자를 지정하지 않으면 기본 값을 대입

   - 기본 인자값을 가지는 인자 다음에는 기본 값이 없는 인자 활용 불가

     ```python
     def greeting(age, name = 'Unknown'):
         print(f'{name} is {age} years old.')
         
     greeting(5)👉 Unknown is 5 years old. 
     greeting(5, 'Pepper')👉 Pepper is 5 years old. 
     ```

   

3. 키워드 인자(Keyword Arguments)

   - 직접 변수의 이름으로 특정 인자를 전달

   - 키워드 인자를 활용한 다음에는 위치 인자 활용 불가

     ```python
     def greeting(age, name = 'Unknown'):
         print(f'{name} is {age} years old.')
     
     greeting(name = 'Pepper', age = 5)👉 Pepper is 5 years old.  
     ```

   

4. 가변 인자 리스트(Arbitrary Argument Lists)

   - 정해지지 않은 여러 개의 인자를 받기 위해 가변 인자 리스트 활용

   - 가변 인자 리스트는 tuple로 처리되며, 매개변수에 `*`로 표현

     ```python
     # 1. 가변 인자 리스트가 매개변수 목록의 마지막인 경우
     def school(prof, *students):
         print(prof)
         print(students)
         
     school('prof', 's', 't', 'u', 'd', 'e', 'n')
     
     # 2. 가변 인자 리스트가 매개변수 목록의 마지막이 아닌 경우
     ## 가변 인자 이후의 변수는 키워드 인자로 지정
     def school(*students, prof):
         print(prof)
         print(students)
         
     school('s', 't', 'u', 'd', 'e', 'n', prof = 'prof')
     ```



5. 가변 키워드 인자(Arbitrary Keyword Arguments)

   - 가변 키워드 인자들은 `dict`로 처리되며, 매개변수에 `**`로 표현

   - 주로 `kwargs`라는 이름을 사용

     ```python
     def greeting(**kwargs):
         return kwargs
     
     greeting(한국어='안녕', 영어='hi', 독일어='Guten Tag')
      👉 {'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
     ```



## 4. Scope

- 함수는 코드 내부에 공간(scope)를 생성

  - 함수로 생성된 공간은 `지역 스코프(local scope)`
  - 그 외에 코드 어디서든 참조할 수 있는 공간은 `전역 스코프(global scope)`

  ```python
  a = 10 # global
  
  def func(b):
      c = 20 # func()의 local
      print('지역스코프입니다.')
      ## local에서는 global variable 사용 가능
      print(a) # 10
      print(b) # 5
      print(c) # 20
  
  func(5)
      
  print('전역스코프입니다.')
  print(a) # 10
  ## global에서는 local variable 사용 불가
  print(b) # 에러
  print(c) # 에러
  ```



- `LEGB Rule`
  - 파이썬에서는 아래와 같은 우선순위로 이름(식별자)를 찾음
    - `L`ocal scope: 정의된 함수
    - `E`nclosed scope: 상위 함수 
    - `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
    - `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성



## 5. 재귀함수 (recursive function)

- 재귀함수는 함수 내부에서 자기 자신을 호출하는 함수

- [example] 팩토리얼 계산

  > 팩토리얼은 1부터 n 까지 양의 정수를 차례대로 곱한 값이며 `!` 기호로 표기합니다. 예를 들어 3!은 3 * 2 * 1이며 결과는 6 입니다.
  >
  > `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성하세요. 
  >
  > n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

---

```python
def factorial(n):
    # base case
    if n == 1:
        return n
    else:
        return factorial(n-1) * n
    
factorial(5)
```