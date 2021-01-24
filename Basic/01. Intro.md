# 01. Intro

## 1. Data Type

> - 숫자 (Number)
> - 문자열 (String)
> - True / False (Boolean)

#### 1. 숫자 (Number)

#####  1. 정수 (`int`, Integer)

- 10진수 외에도 2진수(0b), 8진수(0o), 16진수(0x) 로도 표현 가능

  ```python
  binary_number = 0b10
  octal_number = 0o10
  decimal_number = 10
  hexadecimal_number = 0x10
  print(f"""
  2진수 : {binary_number}
  8진수 : {octal_number}
  10진수 : {decimal_number}
  16진수 : {hexadecimal_number}
  """)
  ```

- 파이썬에서 표현할 수 있는 가장 큰 수는 sys 모듈을 통해 표현 가능

  ```python
  import sys
  max_int = sys.maxsize
  # sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
  print(max_int)
  super_max = sys.maxsize * sys.maxsize
  print(super_max)
  ```



#####  2. 실수 (`float`, Floating point number)

- 컴퓨터가 표현하는 실수를 표현하는 과정에서 부동소수점을 사용

  - 비트(2진수)를 통해 숫자를 표현하는 과정에서 `floating point rounding error` 가 발생할 수 있음

- 실수의 연산과 비교 과정에서 `floating point rounding error` 를 처리하는 방법

  ```python
  x = 0.38
  y = 3.5 = 3.12
  
  # 1. math 모듈을 통해 처리 (주로 사용하는 방법)
  import math
  math.isclose(x, y)
  
  # 2. sys 모듈을 통해 처리
  # epsilon 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
  import sys
  abs(x - y) <= sys.float_info.epsilon
  
  # 3. 작은 수를 통해 처리
  abs(x - y) <= 1e-10
  ```

- `float('inf')`(양의 무한대)와 `float('-inf')`(음의 무한대)도 표현 가능

#####  3. 복소수(`complex`, Complex number)

- 실수부와 허수부를 가지며, 파이썬에서는 허수부를 `j`로 표현

- 실수부와 허수부의 값을 구하는 방법은 아래와 같음

  ```python
  z = (3+4j)
  z.real # 실수부
  z.imag # 허수부
  ```

  



#### 2. 문자열 (String)

* 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능

    - 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`

    - 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`

    - 삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`


* `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하는 것을 권장 (Pick a rule and Stick to it)



#####  1. 이스케이프 시퀀스 

- 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|    \n    |      줄 바꿈      |
|    \t    |        탭         |
|    \r    |    캐리지리턴     |
|    \0    |     널(Null)      |
|   \\\\   |        `\`        |
|   \\'    | 단일인용부호(`'`) |
|   \\"    | 이중인용부호(`"`) |

#####  2. String interpolation

```python
name = 'Pepper'
score = 5

# 1. f-strings (주로 사용하는 방법)
print(f'Hello, {name}. Your score is {score}!')

# 2. str.format()
print('Hello, {}. Your score is {}!'.format(name, score))

# 3. %-formating
print('Hello, %s. Your score is %d!' % (name, score))
```



#### 3. T/F (Boolean)

- `bool` 타입은 `True`와 `False`로 구성되며, 비교/논리 연산을 수행 등에서 활용

- 아래와 같이 값이 없는 것은 `False`로 변환
  - `0, 0.0, (), [], {}, '', None`
  - `None`: 값이 없음을 표현하기 위한 type



## 2. Variable & Operator

#### 1. Variable

* 변수는 `=`을 통해 할당(assignment) 

* 해당 데이터 타입을 확인하기 위해서는 `type()`을, 메모리 주소를 확인하기 위해서는 `id()`를 활용

* **식별자(Identifiers)**: 변수, 함수, 모듈, 클래스 등을 식별하는 데에 사용하는 이름

  * 식별자로 사용할 수 없는 키워드는 아래와 같음

    ```python
    import keyword
    print(keyword.kwlist)
    
    """
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    """
    ```

  * 이 외에도 `내장함수` 나 `모듈` 등의 이름도 식별자로 사용하지 않음



#### 2. Operator

#####  1. 산술 연산자

- `+` (덧셈), `-` (뺄셈), `*` (곱셈), `/` (나눗셈), `//` (몫), `%` (나머지), `**` (거듭제곱)

  - `divmod()`:  나눗셈을 통해 계산된 몫과 나머지를 한 쌍의 숫자로 반환

    - divmod(10, 3) 👉 (10  //  3, 10 % 3) 👉 (3, 1)




#####  2. 비교연산자

- 수학에서 사용하는 비교 연산자(`<`, `>` 등)와 동일
-   추가로, `==` (같음), `!=` (같지 않음), `is` (객체 아이덴티티), `is not` (부정된 객체 아이덴티티) 사용



##### 3. 논리 연산자 

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

- 단축평가: 첫 번째 값이 확실할 때, 두 번째 값은 확인하지 않음으로써 속도 향상
  - `and`는 a가 False이면 a를 리턴하고, True이면 b를 리턴
    - `and`는 모두 True일 경우만 True이기 때문에 a가 True일 때 b도 반드시 확인해야 함
  - `or`는 a가 True이면 a를 리턴하고, False이면 b를 리턴
    - `or`는 하나만 True여도 True이기 때문에 True를 만나면 해당 값을 반환