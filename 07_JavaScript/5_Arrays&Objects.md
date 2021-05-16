# 5. Arrays & Objects



## 1. Arrays

> 키와 속성들을 담고 있는 참조 타입의 객체(object)
>
> - 순서 보장
> - 0을 포함한 양의 정수 인덱스로 특정 값에 접근
> - 배열의 길이는 `array.length`로 접근



#### 1. 기본 배열 조작 Method

| Method          | Description                                          | etc.                    |
| --------------- | ---------------------------------------------------- | ----------------------- |
| reverse         | 원본 배열의 요소들의 순서를 반대로 정렬              |                         |
| push & pop      | 배열의 가장 뒤에 요소를 추가 또는 제거               |                         |
| unshift & shift | 배열의 가장 앞에 요소를 추가 또는 제거               |                         |
| includes        | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환     |                         |
| indexOf         | 배열에 특정 값이 존재하는지 판별 후 해당 인덱스 반환 | 없을 경우 -1 반환       |
| join            | 배열의 모든 요소를 구분자를 매개로 연결              | 구분자 생략 시 쉼표 `,` |



#### 2. Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
  - callback 함수: 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

| Method  | Description                                                  |
| ------- | ------------------------------------------------------------ |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 (반환 값 없음) |
| map     | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환           |
| filter  | 콜백 함수의 반환 값이 `true`인 요소들만 모아 새로운 배열 반환 |
| reduce  | 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환        |
| find    | 콜백 함수의 반환 값이 `true`면 해당 요소를 반환              |
| some    | 배열의 요소 중 하나라도 판별 함수를 통과하면 `true`를 반환   |
| every   | 배열의 모든 요소가 판별 함수를 통과하면 `true`를 반환        |

- `array.forEach(callback(element[, index[, array]]))`

  - break, continue 사용 불가능

  ```javascript
  const students = ['Tim', 'Harry', 'Jackson', 'carol']
  
  students.forEach((name, index) => {
      console.log(name, index)
  })
  ```

  

- `array.map(callback(element[, index[, array]]))`

- `array.filter(callback(element[, index[, array]]))`

  ```javascript
  const nums = [1, 2, 3, 4, 5]
  
  const doulbleNums = nums.map((num) => {
      return num * 2
  })
  
  const oddNums = nums.filter((num) => {
      return num % 2
  })
  
  console.log(doulbleNums) // 👉 [2, 4, 6, 8, 10]
  console.log(oddNums) // 👉 [1, 3, 5]
  ```



- `array.reduce(callback(acc, element, [index[, array]])[, initialValue])`

  - `acc` : 이전 callback 함수의 반환 값이 누적되는 변수
  - `initialValue` : callback 함수 최초 호출 시, acc에 할당되는 값
    - 설정하지 않으면 배열의 첫 번째 값으로 사용

  ```javascript
  const nums = [1, 2, 3, 4, 5]
  
  const sumOfNums = nums.reduce((acc, num) => {
      return acc + num
  }, 0)
  
  console.log(sumOfNums) // 👉 15
  ```

  

- `array.find(callback(element[, index[, array]]))`

  - 찾는 값이 배열에 없으면 `undefined` 반환

  ```javascript
  const students = [
      { name: 'Tim', score: 87}, 
      { name: 'Harry', score: 92},
      { name: 'Jackson', score: 76},
      { name: 'Carol', score: 100},
  ]
  
  const result = students.find((student) => {
      return student.score == 100
  })
  
  console.log(result) // 👉 { name: 'Carol', score: 100}
  ```

  

- `array.some(callback(element[, index[, array]]))`

  - 빈 배열은 항상 `false`

- `array.every(callback(element[, index[, array]]))`

  - 빈 배열은 항상 `true`

  ```javascript
  const nums = [1, 2, 3, 4, 5]
  
  const hasOddNum = nums.some((num) => {
      return num % 2
  })
  
  const isEveryNumsOdd = nums.every((num) => {
      return num % 2
  })
  ```

  

#### 3. 배열 순회 방식

```javascript
const animals = ['Cat', 'Dog', 'Lion', 'Tiger', 'Snake', 'Bird']

// 1. for loop
for (let i = 0; i < animals.length; i++) {
    console.log(i, animals[i])
}

// 2. for - of
for (animal of animals) {
    console.log(animal)
}

// 3. forEach
animals.forEach((animal, index) => {
    console.log(index, animal)
})
```



## 2. Objects

> 속성의 집합으로, 중괄호 내부에 key-value 쌍으로 표현 
>
> - key는 문자열 타입 (구분자가 있을 경우 따옴표로 묶어서 표현)
> - value는 모든 타입



 #### 1. 객체 생성 및 조작 문법

1. 속성명 축약

   - 객체 정의 시, key와 할당하는 변수 이름이 같으면 축약 가능

     ```javascript
     let fruits = ['apple', 'orange', 'banana', 'lemon']
     let vagetables = ['mushroom']
     
     const market = {
         fruits,
         vegetables,
     }
     ```

     

2. 메서드명 축약

   - 메서드 선언시 function 키워드 생략 가능

     ```javascript
     const greeting = {
         hello() {
             console.log('Hello!')
         }
     }
     ```

     

3. 계산된 속성 사용

   - 객체 정의 시 key 이름을 표현식을 통해 동적으로 생성 가능

     ```javascript
     const firstCat = 'pepper'
     const secondCat = 'kanda'
     const myCats = {
         [firstCat]: 5,
         [secondCat.toUpperCase()]: 3,
     }
     
     console.log(myCats) // 👉 {pepper: 5, KANDA: 3}
     ```

     

4. 구조 분해 할당

   - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

     - key와 변수 명이 같을 경우 사용 가능

     ```javascript
     const info = {
         name: 'Pepper',
         age: 5, 
         color: 'Grey'
     }
     
     const { name } = info
     const { age, color } = info
     ```



## 3. JSON

> JavaScript Object Notation
>
> - key-value 쌍 형태의 데이터를 표기하는 언어 독립적 표준 포맷
>   - 자바스크립트 객체(objects)와 유사하게 생겼으나, 실제로는 **문자열 타입**
> - JSON을 조작하기 위한 두 가지 내장 메서드
>   - `JSON.parse()` 👉 JSON > 자바스크립트 객체
>   - `JSON.stringify()` 👉 자바스크입트 객체 > JSON

