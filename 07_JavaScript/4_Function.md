# 4. Function

> - 자바스크립트 함수는 일급 객체(First-class citizens)
>   - 변수에 할당 가능
>   - 함수의 매개변수로 전달 가능
>   - 함수의 반환 값으로 사용 가능



## 1. 함수 선언식

- 함수의 이름과 함께 정의하는 방식

  - 익명 함수 불가능, 호이스팅 O

  ```javascript
  function name (args) {
      // do something 
  }
  ```

  

## 2. 함수 표현식

- 힘수를 표현식 내에서 정의하는 방식

  - 함수 이름을 생략하고 익명 함수로 정의 가능, 호이스팅 X
  - Airbnb Style Guide 권장 방식

  ```javascript
  const myFunction = function (args) {
      // do something
  }
  ```

  

#### cf. 함수 선언식 vs 함수 표현식

1. 호이스팅

   ```javascript
   // 1. 함수 선언식 👉 호이스팅 O
   
   plus(2, 5) // → 7
   
   function plus (num1, num2) {
       return num1 + num2
   }
   
   // 2. 함수 표현식 👉 호이스팅 X
   minus(5, 2) // → Uncaught ReferenceError
   
   const minus = function (num1, num2) {
       return num1 - num2
   }
   ```

   

## 3. 화살표 함수 (Arrow Function)

- 함수를 비교적 간결하게 정의할 수 있는 문법

  1. function 키워드 생략 가능

  2. 함수의 **매개변수가 하나** 뿐이면 `()`도 생략 가능
  3. 함수 바디에 표현식 하나라면 `{}`과 `return` 생략 가능

- [example]

  ```javascript
  // 0. 함수 표현식
  const greeting = function (name) {
      return `hello, ${name}`
  }
  
  // 1. function 생략
  const greeting = (name) => { return `hello, ${name}` }
  
  // 2. () 생략
  const greeting = name => { return `hello, ${name}` }
  
  // 3. {} & return 생략
  const greeting = name => `hello, ${name}`
  ```

  