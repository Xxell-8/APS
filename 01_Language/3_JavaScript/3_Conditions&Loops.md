# 3. Conditions & Loops



## 1. Conditions

#### 1. if statement

- 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓 판단

  ```javascript
  if (condition) {
      // do something
  } else if (condition) {
      // do something
  } else {
      // do something
  }
  ```



#### 2. switch statement

- 조건 표현식의 결과 값이 어느 값(case)에 해당하는지 판별

  - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우, if문보다 가독성이 나을 수 있음

  ```javascript
  switch(expression) {
      case 'first value': {
        // do something
        break
      }
      case 'second value': {
        // do something
        break
      }
      default : {
        // do something
      }
  }
  ```

  - `break`, `default` 문은 선택적으로 사용 가능
    - break문이 없는 경우,  break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행



#### cf. `if` vs `switch`

```javascript
const numOne = 100
const numTwo = 7
let operator = '+'

// 1. if statement
if (operator == '+') {
  console.log(numOne + numTwo)
} else if (operator == '-') {
  console.log(numOne - numTwo)
} else if (operator == '*') {
  console.log(numOne * numTwo)
} else if (operator == '/') {
  console.log(numOne / numTwo)
} else {
  console.log('올바른 연산자를 입력해주세요.')
}

// 2. switch statement
switch(operator) {
  case '+': {
    console.log(numOne + numTwo)
    break
  }
  case '-': {
    console.log(numOne - numTwo)
    break
  }
  case '*': {
    console.log(numOne * numTwo)
    break
  }
  case '/': {
    console.log(numOne / numTwo)
    break
  }
  default: {
    console.log('올바른 연산자를 입력해주세요.')
  }
}
```



## 2. Loops

#### 1. while

- 조건문이 참인 동안 반복 시행

  ```javascript
  let num = 0
  
  while (num < 10) {
    console.log(num)
    num += 1
  }
  ```

  

#### 2. for

- 세미콜론 `;` 으로 구분되는 세 부분으로 구성

  - initialization : 최초 반복문 진입 시 1회만 실행

  - condition : 매 반복 시행 전 평가되는 부분

  - expression : 매 반복 시행 이후 평가되는 부분

    ```javascript
    for (initialization; condition; expression) {
      // do something
    }
    ```

  ```javascript
  for (let num = 0; num < 10; num++) {
    console.log(num)
  }
  ```



#### 3. for - in

-  객체(object)의 속성들을 순회할 때 사용

  - 배열 순회도 가능하나 권장하지 않음

  ```javascript
  const animals = {
      Pepper: 'tiger',
      Kanda: 'cat',
      Tony: 'dog'
  }
  
  for (let animal in animals) {
      console.log(animal)
  }
  ```

  

#### 4. for - of

- 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용

  ```javascript
  const animals = ['Pepper', 'Kanda', 'Tony']
  
  for (let animal of animals) {
      console.log(animal)
  }
  ```

  