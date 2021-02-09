# CSS Layout

> - 웹 페이지에 포함되는 요소들을 취합하고, 그것들이 어느 위치에 놓일 것인지를 제어하는 기술
> - Float / Flexbox / Grid



## 1. Float

> - Float된 이미지의 좌·우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입
> - 정상 흐름으로부터 벗어난 요소의 주위를 텍스트 및 인라인 요소가 감싸 좌·우측을 따라 배치되는 것을 지정



####  1. Float 속성

- `float: none` (default)
- `float: left` (해당 요소를 왼쪽으로 띄움)
- `float: right` (해당 요소를 오른쪽으로 띄움)



####  2. clearfix

- float 요소와 block 요소 간의 레이아웃이 깨지는 것을 방지하기 위한 기능

  ```css
  .clearfix::after {
    content: "";
    display: block;
    clear: both;
  }
  ```

  - float 속성을 적용한 요소의 **부모 요소**에 적용
  - 부모 태그 다음에 가상 요소로 내용이 빈 블럭을 만드는 것



## 2. Flexible Box

> - 요소 간의 공간 배분과 정렬 기능을 위한 1차원 레이아웃



####  1. Flexbox 기본 개념

- 요소
  - Flex Container (부모 요소)
    - 부모 요소에 `display: flex`를 작성
  - Flex Item (자식 요소)
- 축
  - main axis (메인 축)
  - cross axis (교차 축)



####  2. Flexbox 속성

- 배치 방향 설정
  - `flex-direction` (메인 축의 방향을 설정)
    1. `row` (default) →
    2. `row-reverse` ←
    3. `column` ↓
    4. `column-reverse` ↑



- 메인축 방향 정렬

  - `justify-content`

  

- 교차축 방향 정렬

  - `align-items`
  - `align-self`
  - `align-content`

- 기타

  - `flex-wrap`
  - `flex-flow`
  - `flex-grow`
  - `order`

  