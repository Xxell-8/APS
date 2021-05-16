# `this` in JavaScript

> 함수 호출 방식에 의해 결정되는 `this`
>
> - 자바스크립트는 해당 함수 호출 방식에 따라 this에 바인딩되는 객체가 달라짐
> - 즉, 함수를 선언할 때 this의 객체가 결정되는 게 아니라, **함수를 어떻게 호출하는지에 따라 동적으로 결정**되는 것



## 1. 함수 호출 방식

#### 1. 함수 호출

> 전역 객체는 모든 객체의 유일한 최상위 객체를 의미하며, 일반적으로 Browser에서는 `window`

```js
const checkThis = function () {
    console.log(this)
}

checkThis() // 👉 window
```

- 기본적인 함수 선언을 하고, 전역에서 호출할 경우 전역 객체가 바인딩



#### 2. 메서드 호출

```js
const user = {
    name: 'pepper',
    checkThis,
}

user.checkThis() // 👉 {name: "pepper", checkThis: ƒ}
```

- 메서드로 선언하고 호출할 경우, 객체의 메서드이므로 해당 객체가 바인딩



#### 3. Arrow Function

> - 화살표 함수는 호출 위치와 상관없이 상위 스코프를 가리킴
>   - Lexical scope
>     - 함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정

```js
const checkArrowThis = () => {
    console.log(this)
}

const user = {
    name: 'kanda',
    checkArrowThis,
}

checkArrowThis() // 👉 window
user.checkArrowThis() // 👉 window
```

- 메서드 선언을 화살표 함수로 하면, 해당 객체의 상위 스코프인 전역 객체가 바인딩

  - checkArrowThis() 함수가 애초에 전역에서 선언되었기 때문

    👉 **메서드 선언은 function 키워드**를 통해 정의해야 함



## 2. ES6에서의 화살표 함수

#### 1. 함수 내 함수

- function 키워드

  ```js
  const zoo = {
      animals: ['Lion'],
      print: function () {
          console.log(this) // {animals: Array(1), print: ƒ}
          console.log(this.animals) // ["Lion"]
          this.animals.forEach(function (animal) {
              console.log(animal) // Lion
              console.log(this) // window
          })
      }
  }
  
  zoo.print()
  ```

  - 전역에서 호출되었기 때문에 forEach의 콜백 함수에서 this에는 전역 객체인 window 바인딩

  

- 화살표 함수

  ```js
  const zoo = {
      animals: ['Lion'],
      print: function () {
          console.log(this) // {animals: Array(1), print: ƒ}
          console.log(this.animals) // ["Lion"]
          this.animals.forEach((animal) => {
              console.log(animal) // Lion
              console.log(this) // {animals: Array(1), print: ƒ}
          })
      }
  }
  
  zoo.print()
  ```

  - print 메서드 내에 forEach의 콜백함수에서의 상위 스코프는 zoo 객체

    - 호출 위치와 관계 없이 선언 위치의 상위 스코프를 가리키는 화살표 함수는 this에 zoo가 바인딩

      👉 **함수 내의 함수 상황에서는 화살표 함수**를 쓰는 것이 좋음



#### 2. 이벤트 리스너

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="function">function</button>
  <button id="arrow">arrow function</button>
  <script>
    const functionButton = document.querySelector('#function')
    const arrowButton = document.querySelector('#arrow')
    
    functionButton.addEventListener('click', function(event) {
      console.log(this) // <button id="function">function</button>
    })
    arrowButton.addEventListener('click', event => {
      console.log(this) // window
    })
  </script>
</body>
</html>
```

- addEventListener에서의 콜백 함수는,

  -  특별하게 function 키워드의 경우에 이벤트 리스너를 호출한 대상을( event.target ) 뜻함

    👉 따라서, 호출한 대상을 원한다면 this 를 활용할 수 있음

  - 다만, 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨

- **이벤트 리스너의 콜백 함수는 function 키워드**를 사용