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
    - `flex-start` `flex-end` `center` `space-between` `space-around` `space-evenly`

  

- 교차축 방향 정렬

  - `align-items`
    - `flex-start` `flex-end` `center` `baseline` `stretch`
  - `align-self`
  - `align-content`

- 기타

  - `flex-wrap` : items를 강제로 한 줄에 배치되게 할 지 설정
    - `nowrap` (default) : 모든 아이템들 한 줄에 배치
    - `wrap` : 자리가 없으면 다음 줄로 배치
    - `wrap-reverse` : 넘치면 그 윗줄로 배치(역순)
  - `flex-flow` : flex-direction 과 flex-wrap 의 shorthand
  - `flex-grow` : main 축에서 남는 공간을 각 items에 분배
  - `order`
    - 기본값 0, 작은 숫자일수록 앞으로 이동

  

## 3. Bootstrap

> The most popular HTML, CSS, and JS library in the world

- Responsive Web Design
  - layout은 User의 사용 환경을 고려해야 함
    - 스마트폰이나 태블릿 등 모바일 기기는 화면이 작기 때문에 가독성에 더욱 신경
  - 데스크탑용, 테블릿용, 모바일용 웹사이트를 별도로 구축할 수도 있지만 One Source Multi Use의 관점에서 올바른 해결책은 아니다.
  - 반응형 웹 디자인(Responsive Web Design)은 화면 해상도에 따라 가로폭이나 배치를 변경하여 가독성을 높여 이러한 문제를 해결
    - 즉, 하나의 웹사이트를 구축하여 다양한 디바이스의 화면 해상도에 최적화된 웹사이트를 제공 



####  + Bootstrap Grid System

- Grid System
  - 부트스트랩의 grid system 은 containers, rows, columns 를 사용해서 컨텐츠를 레이아웃하고 정렬
  - 모바일 우선 flexbox grid 를 사용하여 **12개의 column 시스템**
    - 12는 약수가 많기 때문에 다양한 레이아웃을 구성할 수 있음

  - `.container` 👉 `.row` 👉 `col-`



- `.row`
  - row 는 columns 의 wrapper 이다.
  - 각 column에는 공간 사이를 제어하기 위한 좌우 padding 값이 있는데 이를 `gutter` 라고도 한다.
    - row 의 margin 값과 gutter 를 제거하려면 .row 에 `.no-gutters` class 를 사용



- `.col `
  - column class 는 row 당 가능한 12개 중 사용하려는 columns 수
  - columns 너비는 백분율로 설정 되므로 항상 부모 요소를 기준으로 유동적으로 크기가 조정



- offset
  - `offset-{size}` 은 지정한 만큼의 column 공간을 무시하고 다음 공간부터 컨텐츠를 적용



- Nesting
  - `.row` 👉 `.col` 👉 `.row` 👉 `.col` 의 방식으로 중첩 사용 가능



- **Grid breakpoints**
  - 부트스트랩 grid system 은 다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점을 정해 두었는데 이를 breakpoints 라고 한다.
  - 부트스트랩은 대부분의 크기를 정의하기 위해 em 또는 rem 을 사용하지만 px 는 그리드  breakpoint 에 사용된다. (뷰포트 너비가 픽셀 단위이고 글꼴 크기에 따라 변하지 않기 때문)

