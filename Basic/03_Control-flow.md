# 03. Control flow

> **제어문**은 코드 실행의 순차적인 흐름을 제어하는 것인데, 크게 **조건문**과 **반복문**으로 분류



## 1. Conditional Statement

- `if` 조건문은 반드시 **T/F를 판단할 수 있는 조건**과 함께 사용

- `if` 조건문의 기본 구조

  - `expression`에는 일반적으로 참/거짓에 대한 조건식

  ```python
  if <expression>:
      <코드 블럭>
  else:
      <코드 블럭>
  ```

  - 조건이 True이면, `:` 이후의 문장을 수행
  - 조건이 False이면, `else:` 이후의 문장을 수행

- `elif` 로 2개 이상의 조건 활용 가능

  ```python
  if <expression>:
      <코드 블럭>
  elif <expression>:
      <코드 블럭>
  else:
      <코드 블럭>
  ```

- cf. `조건 표현식` 은 조건에 따라 값을 정할 때 활용

  ```python
  # 홀수와 짝수를 구분하는 코드를 쓴다고 할 때,
  
  num = 5
  # if 조건문의 경우,
  if num % 2:
      print('odd')
  else:
      print('even')
      
  # 조건 표현식의 경우,
  print('odd') if num % 2 else print('even')
  ```

  

## 2. Loop Statement

#### 1. `for` 반복문

- `for` 문은 시퀀스(string, tuple, list, range)나 다른 순회가능한 객체(iterable)의 요소들을 순회

- cf. `enumerate()`를 활용하면, `index`와 `value`를 함께 쓸 수 있음

  - `enumerate(iterable, start=0)`

    ```python
    students = ['Tom', 'Jerry', 'Nick', 'Sam']
    
    for idx, student in enumerate(students):
        print(idx, student)
        
    👉 0 Tom
    	1 Jerry
        2 Nick
        3 Sam
    ```

    

#### 2. `while` 반복문

- `while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행
  - **반드시 종료조건을 설정**

  

#### + for 문과 while 문 비교

- [example] 1부터 N까지의 총합을 구하는 코드

  ```python
  N = 10
  
  # for 문
  total = 0
  for i in range(1, N+1):
      total += i
  print(total)
  
  # while 문
  total = 0
  i = 1
  while i <= N:
      total += i
      i += 1
  print(total)
  ```

  

## 3. Cotrol Flow

#### 1. `break`

- `break`는 반복문을 종료하고, `for` 나 `while` 문에서 빠져 탈출

- [example] animals 리스트에서 '호랑이'가 나왔을때 반복을 멈추고 '어흥!' 하는 코드

  ```python
  animals = ['고양이', '강아지', '호랑이', '고라니']
  
  for animal in animals:
      print(animal)
      if animal == '호랑이':
          print('어흥!')
          break
  ```



#### 2. `continue`

- `continue`는 `continue` 이후의 코드를 수행하지 않고, 다음 요소부터 계속 반복

- [example] students 딕셔너리에서 60점 이상인 학생만 출력하는 코드

  ```python
  students = {'Tom': 70, 'Jerry': 55, 'Nick': 47, 'Sam': 90}
  
  for student, score in students.items():
      if score < 60:
          continue
      print(f'{student}은 시험에 통과했습니다.')
  ```

- cf. `pass`는 문법적으로 문장이 필요하지만 특별히 넣을 문장이 없을 때 자리를 채우는 용도로 활용 👉 `pass`는 아무것도 하지 않음



#### 3. `for-else`

- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행
- 반복문이 **`break` 문으로 종료될 때는 실행되지 않음
  - 즉, `break`를 통해 중간에 종료되지 않은 경우만 실행

- [example] numbers 리스트에 7이 있을 경우 `True`를, 없을 경우 `False`를 출력하는 코드

  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  
  for number in numbers:
      if number == 7:
          print(True)
          break
  else:
      print(False)
  ```

  