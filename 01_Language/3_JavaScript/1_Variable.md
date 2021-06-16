# 1. Variable

> - 자바스크립트에서 변수를 선언하는 키워드
>
>   | 키워드  | 재선언 | 재할당 | 스코프 |   etc.   |
>   | :-----: | :----: | :----: | :----: | :------: |
>   |  `let`  |   X    |   O    |  블록  | ES6 도입 |
>   | `const` |   X    |   X    |  블록  | ES6 도입 |
>   |  `var`  |   O    |   O    |  함수  |  권장 X  |



## 1. 식별자 (Identifier)

> - 변수를 구분할 수 있는 변수명
> - 반드시 문자, `$`, `_`로 시작해야 하며, 클래스명 외에는 모두 소문자로 시작



####  🚩 식별자 작성 스타일

1. 카멜 케이스(`camelCase`, lower-camel-case)

   - 변수, 객체, 함수에 사용

     ```javascript
     // [example]
     let variableName
     const userInfo = { name: 'pepper', age: 5 }
     function getUserName () {}
     ```

2. 파스칼 케이스(`PascalCase`, upper-camel-case)

   - 클래스, 생성자에 사용

     ```javascript
     // [example]
     class User {
       constructor(options) {
         this.name = options.name
       }
     }
     const person = new user({
       name: 'Pepper'
     })
     ```

     

3. 대문자 스네이크 케이스(`SNAKE_CASE`)

   - 상수(개발자의 의도와 상관없이 변경될 가능성이 없는 값)에 사용

     ```javascript
     // [example]
     const API_KEY = 'adslhalf-wrljr21'
     const PI = Math.PI
     ```



## 2. 변수 선언

#### 1. 기본 개념

1. 선언(Declaration)
   - 변수를 생성하는 행위 또는 시점
2. 할당(Assignment)
   - 선언된 변수에 값을 저장하는 행위 또는 시점
3. 초기화(Intialization)
   - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점



#### 2. 변수 선언 키워드

| `let`                                                        | `const`                                                      | `var`                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| - 변수 재할당 가능<br />- 변수 재선언 불가능<br />- 블록 스코프 | - 변수 재할당 불가능<br />- 변수 재선언 불가능<br />- 블록 스코프 | - 변수 재할당 가능<br />- 변수 재선언 가능<br />- 함수 스코프 |

- `let` vs `const`

  ```javascript
  // 1. 차이점 👉 재할당
    // 1) let - 재할당 가능
    let number = 1
    number = 2
    console.log(number) // → 2
  
    // 2) const - 재할당 불가능
    const number = 1
    number = 2 // → Uncaught TypeError
  
  // 2. 공통점
  	// 1) 재선언 불가능 
    let number = 1
    let number = 2 // → Uncaught SyntaxError
    const number = 1
    const number = 2 // → Uncaught SyntaxError
    
    // 2) 블록 스코프
    let name = 'Pepper'
    if (name === 'Pepper') {
      let name = 'Kanda'
      console.log('블록 스코프:', name) // 블록 스코프: Kanda
    }
    console.log('전역 스코프:', name) // 전역 스코프: Pepper
  
    const name = 'Pepper'
    if (name === 'Pepper') {
      const name = 'Kanda'
      console.log('블록 스코프:', name) // 블록 스코프: Kanda
    }
    console.log('전역 스코프:', name) // 전역 스코프: Pepper
  ```



- `var`

  - **호이스팅**되는 특성으로 인해 예기치 못한 문제 발생 가능

    - 변수를 선언 이전에 참조할 수 있는 현상으로, 선언 이전의 위치에서 접근 시 `undefined` 반환

      ```javascript
      console.log(name) // undefined
      var name = 'Pepper'
      
      // 선언 이전에 접근하면, 아래와 같은 방식으로 인식
      var name // → 선언문이 위로 끌어올려지는 것
      console.log(name) // undefined
      name = 'Pepper'
      ```