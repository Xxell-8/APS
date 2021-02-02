# 05. Error exception

> - 에러(Error)
> - 예외 처리(Exception Handling)



## 1. Error

- [예외 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)



## 2. Exception Handling

####  1. `try-except`

- 기본 구조

  ```python
  try:
      <코드 블럭 1>
  except 예외 as err:
      <코드 블럭 2>
  else:
      <코드 블럭 3>
  finally:
      <코드 블럭 3>
  ```
  - `try` 아래의 코드 블럭 실행

    👉 예외가 발생하면 남은 부분을 수행하지 않고 `except` 실행

  - 여러 개의 `except`를 사용할 경우

    - 에러가 순차적으로 수행되기 때문에 예외 계층 구조에서 가장 작은 범주부터 예외 처리

  - `else`는 에러가 발생하지 않는 경우에 수행되는 문장

    - try 절이 예외를 일으키지 않을 때 실행되어야 하는 코드
    - `else`는 try -except 문에 의해 보호되고 있는 코드가 `일으키지 않은 예외`를 우연히 잡게 되는 것을 방지
      - ① 에러 발생의 가능성이 있는 코드나 ② 예외 처리를 원하는 코드를 try문에 넣어 예외 처리(보호)를 하고, 나머지 부분은 else문에 분리

  - `finally`는 예외의 발생 여부와 관계없이 try 문을 떠날 때 무조건 실행

    - 모든 상황에 실행되어야 하는 코드



####  2. Exception Raising

- `raise`를 활용해 예외를 강제로 발생시킬 수 있음

  ```python
  print('Start')
  raise ZeroDivisionError('division by 0!')
  print('End')
  👉 Start
     ZeroDivisionError: division by 0!
     # Error raise를 하면 그 자리에서 코드가 STOP
  ```



- (참고) `assert` 문은 상태를 검증하는 데에 사용

  - 무조건 `AssertionError`가 발생

  ```python
  assert len(['pepper', 'kanda']) == 1, '길이가 1이 아닙니다.
   👉 AssertionError: 길이가 1이 아닙니다. 
  ```

  

