# 08. OOP

> - 객체 지향 프로그래밍(Object Oriented Programming)
> - 객체(Object)와 클래스(Class)



## 1. 개념정리

1. Object
   - 객체는 고유의 속성을 가지며 클래스에 정의한 행위를 수행
2. Class
   - 공통된 속성과 행위를 정의한 것으로 객체지향 프로그램의 기본적인 **사용자 정의 데이터형**
3. Instance
   - 특정 `class`로부터 생성된 해당 클래스의 실체
4. Attribute
   - 클래스나 인스턴스가 가지는 속성
5. Method
   - 클래스나 인스턴스에 적용가능한 조작법
   - 클래스나 인스턴스가 할 수 있는 행위



## 2. 객체(Object)

- Python에 존재하는 모든 것은 객체(object)
- 객체(Object)의 특징
  - **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가? 
  - **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
  - **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?



#### 1. Type & Instance

- `type`이란, 공통된 속성과 조작법을 가진 객체들의 분류
- `instance`는 특정 타입(type)의 실제 데이터 예시
  - 파이썬에서는 모든 것이 `객체`이고, 모든 객체는 `특정 타입의 인스턴스`
    - a = 1일때, a는 객체이면서 `int` 타입의 인스턴스



#### 2. Attribute & Method

- `Attribute`란, 객체의 상태/데이터

  ```python
  complex_num = 1+2j
  print(type(complex_num)) 👉 <class 'complex'>
  
  # complex 객체는 실수 속성과 허수 속성을 가짐
  print(complex_num.real, complex_num.imag) 👉 1.0 2.0
  ```

- `Method`란, 특정 객체에 적용할 수 있는 행위



## 3. Object-Oriented Programming

> OOP는 Object가 중심이 되는 프로그래밍으로, 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것이다.

- OOP의 특징

  - 코드의 **직관성**
    - 보다 직관적인 코드 분석 가능
  - 활용의 **용이성**
    - SW 개발과 보수의 간편화
  - 변경의 **유연성**
    - 프로그램의 유연화 + 변경의 용이성

- 프로그래밍의 패러다임

  ```python
  'pepper'.capitalize() #객체지향 (단축형)
   -> str.capitalize('pepper') #절차지향
  ```

  - 즉, 데이터가 흘러 다니는 것으로 보는 시각에서 데이터가 중심이 되는 시각으로 변한 것

  - 파이썬은 객체 지향 언어지만, 절차 지향 언어도 사용



## 4. Class

> - `class`란, 객체들의 분류(class)를 정의할 때 쓰이는 키워드
> - `type`이란, 공통 속성을 가진 객체들의 분류(class)



- `클래스 이름`은 `PascalCase(UpperCamelCase)` 사용
  - cf. 변수나 함수 이름은 snake_case

- 클래스 내부에는 데이터(속성)와 함수(메서드)를 정의

  ```python
  class NewClass:
      pass
  
  example = NewClass()
  print(type(example)) 
   👉 <class '__main__.NewClass'>
  print(type(NewClass))
   👉 <class 'type'>
      
  # metaclass(type)  - 재귀적으로 자기 자신을 생성
  print(type(type))
   👉 <class 'type'>
  ```

- 클래스는 `블루프린트(청사진)`이다
  - 클래스 하나로 여러 가지 인스턴스를 만드는 것
  - 각각의 인스턴스는 서로 **독립적**
    - 독자적인 이름 공간이 생기는 것



- 클래스의 기본 구조

  ```python
  class Person:
      population = 0
      
      def __init__(self, name, age):
          self.name = name
          self.age = age
          Person.population += 1
      
      def introduce(self):
          return f'안녕하세요! {self.age} 살, {self.name} 입니다.'
      
      @classmethod
      def get_population(cls):
          return f'현재 인구는 {cls.population} 입니다.'
      
      @staticmethod
      def info():
          return 'Person class를 만들고 있습니다.'
      
      def __del__(self):
          Person.population -= 1
  ```

  

- `매직메서드`
  - 더블 언더스코어(`__`)가 있는 메서드로, 특별한 일을 하기 위해 만들어진 메서드
    - `__init__` : 인스턴스 객체가 생성될 때 호출되는 함수
    - `__del__` : 인스턴스 객체가 소멸되기 직전에 호출되는 함수
    - `__str__` : 특정 객체를 출력(`print()`)할 때 보여줄 내용을 정의하는 함수
    - 이 외에도 다양한 매직메서드가 존재



- 메서드의 종류는 `instance method`, `class method`, `static method`
  - 인스턴스는 3가지 메서드 모두에 접근 가능
    - BUT 인스턴스에서 클래스 메서드와 스태틱 메서드 호출하지 말기
    - 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계
  - 클래스 또한 3가지 메서드 모두에 접근 가능
    - BUT 클래스에서 인스턴스 메서드는 호출하지 말기
    - 클래스가 할 행동은 다음 원칙에 따라 설계
         - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의
         - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의
              - 정적 메서드는 `cls`, `self`와 같이 묵시적인 첫번째 인자를 받지 않기 때문



## 5. 상속

- 클래스는 `상속`이 가능

  - 부모 클래스의 모든 속성이 자식 클래스에게 상속되어 재사용성 ☝

  ```python
  class Person:
      population = 0
      
      def __init__(self, name='Unknown'):
          self.name = name
          Person.population += 1
          
      def greeting(self):
          print(f'Hi! My name is {self.name}.')
    
  
  class Student(Person):
      def __init__(self, name, student_id):
          super().__init__(name)
          self.student_id = student_id
  ```



- 클래스와 상속관계에서의 `이름 공간`
  - 인스턴스 👉 자식 클래스 👉 부모 클래스 👉 전역 순으로 이름 공간을 탐색
  - `class.mro()` : 메서드를 가져오는 순서



- `다중 상속` 도 가능

  ```python
  class Person:
      def __init__(self, name):
          self.name = name
      def info(self):
          print('사람입니다.')
          
  class Mom(Person):
      gene = 'XX'
      def talk(self):
          print('엄마 왔다!!!!')
          
  class Dad(Person):
      gene = 'XY'
      def sing(self):
          print('아빠 곰은 뚱뚱해')
          
  class Girl(Mom, Dad):
      def sing(self):
          print('아기 곰은 너무 귀여워')
          
  class Boy(Dad, Mom):
      def cry(self):
          print('으앙')
          
  first_baby = Girl('Tommy')
  second_baby = Boy('Jerry')
  
  # 상속 받을 class을 정의하는 순서에 따라 이름 공간 탐색 순서가 변동
  print(first_baby.gene) 👉 'XX'
  print(second_baby.gene) 👉 'XY'
  ```

  

