# CSS

> - Cascading Style Sheets
>- 스타일, 레이아웃 등을 통해 HTML이 문서(HTML)를 표시하는 방법을 지정하는 언어



## 1. 기본 구조

```css
h1 {
    color: blue;
    font-size: 15px;
}
```

- CSS 구문의 기본 구조
  - 스타일을 지정할 요소를 지정하는 **선택자**와 함께 시작
  - 중괄호 안에 스타일의 **속성**과 **값**을 쌍으로 하는 선언

- CSS 정의 방법
  1. `Inline style`
     - 해당 태그에 직접 style 속성을 적용
  2. 내부 참조 (`Embedding style`)
     - `<head>`에 `<style>` 태그 작성
  3. 외부 참조 (`Link style`)
     - 외부 CSS 파일을 만들고 `<head>`에 `<link>`로 불러오기



## 2. CSS Selector

####  1. Selector

- 기본 선택자
  - 전체 선택자 (`*`)
  - 요소 선택자
  - 클래스 선택자 (`.classname`)
  - 아이디 선택자(`#idname`)
    - 아이디는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용
- 결합자
  - 자손 결합자
    - `A B`: 선택자 A의 **모든 자손** 요소 중 선택자 B와 일치하는 요소를 선택
  - 자식 결합자
    - `A>B` : 선택자 A의 **자식** 요소 중 선택자 B와 일치하는 요소를 선택 
  - 일반 형제 결합자
    - `A~B` : 선택자 A의 형제 요소 중 A 뒤에 위치하는 모든 선택자 B 요소를 선택
  - 인접 형제 결합자
    - `A+B` : 선택자 A의 형제 요소 중 A 바로 뒤에 위치하는 선택자 B 요소를 선택
    - 단, A와 B 사이에 다른 요소가 존재하면 선택되지 않음

- 의사 클래스/요소
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스



####  2. Cascading Order

- CSS 적용 우선 순위
  - `!important` 👉 inline-style 👉 id 선택자 👉 **class 선택자** 👉 요소 선택자 (+ 소스 순서)



####  3. CSS 상속

- CSS는 부모 요소의 속성이 자식에게 상속되는데,
  - 상속되는 속성
    -  text 관련 요소(font, color, text-align)
    - opacity, visibility
  - 상속되지 않는 속성
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left/z-index)



## 3. CSS 단위

####  1. (상대) 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀'을 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 가변적인 레이아웃에서 자주 사용되는 백분율 단위
- em
  - 요소에 지정된 사이즈에 상대적인 사이즈를 가지는 배수 단위
  - 상속의 영향을 받으며, 상황에 따라 각기 다른 값을 가질 수 있음
- rem
  - 최상위 요소인 `html(root em)`을 기준으로 하는 배수 단위
  - 상속의 영향을 받지 않음
- Viewport 기준 단위
  - vw, vh, vmin, vmax



####  2. 색상 표현 단위

- 색상 키워드
  - red, blue, black과 같이 특정 색을 지칭
- RGB 색상
  - 16진수 표기법(#000000)이나 함수형 표기법(rgb(0, 0, 0))으로 사용
  - a는 alpha(투명도)가 추가
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색상을 표현
  - a는 alpha(투명도)가 추가



## 4. CSS Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정

- 모든 HTML 요소는 **box** 형태
- 하나의 박스는 네 부분(영역)으로 이루어 진다.
  - content / padding / border / margin
- CSS는 기본적으로 content-box를 기준으로 Sizing
  - border-box를 기준으로 하려면 `box-sizing: border-box`로 설정



1. Content
   - 글이나 이미지 등 요소의 실제 내용

2. Padding

   - 테두리 안쪽의 내부 여백

3. Border

   - 테두리 영역

4. Margin

   - 테두리 바깥의 외부 여백

   ```css
   .margin {
       margin-top: 10px;
       margin-right: 10px;
       margin-bottom: 10px;
       margin-left: 10px;
   }
   ```

   - Shorthand

     ```css
     margin: 10px; # 상하좌우
     margin: 10px 20px; # 상하/좌우
     margin: 10px 20px 30px; # 상/좌우/하
     margin: 10px 20px 30px 40px; # 상/우/하/좌
     ```

     

- **마진 상쇄**
  - block의 top 및 bottom margin이 때로는 (결합되는 마진 중 크기가) 가장 큰 한 마진으로 결합(상쇄(collapsed))



## 5. CSS Display

- `display:block`
  - 화면 크기 전체의 가로 폭을 차지(줄 바꿈이 일어나는 요소)
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - div / ul, ol, li / p / hr / form 등



- `display:inline`
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top, margin-bottom 지정 불가
  - 상하 여백은 line-height로 지정
  - span / a / img / input, label / b, em, i, strong 등



- `display:inline-block`
  - inline과 block 레벨 요소의 특징을 모두 가짐



- `display: none`
  - 해당 요소를 화면에 표시하지 않음 
    - 해당 요소의 공간도 사라짐
  - cf. `visibility: hidden;`
    - 해당 요소를 화면에 표시하지 않지만
    - 해당 요소의 **공간은 존재**



## 6. CSS Position

- 문서 상에서 요소를 배치하는 방법을 지정



1. `static`
   - 모든 태그의 기본 default 값
2. `position:relative`
   - static 위치를 기준으로 좌표 속성을 사용해 위치 이동
3. `position:absolute`
   - **static이 아닌** 부모/조상 요소를 기준으로 좌표 속성 만큼 이동
   - 부모 요소를 찾아가다가 없으면 body에 붙음
   - `absolute`는 원래 위치(static)에 있던 공간이 사라짐
     - 즉, 다른 모든 것과는 별개로 독자적인 곳에 위치
   - 다른 요소의 위치와 격리된 사용자 인터페이스 기능에 사용
     - 팝업 정보 상자 및 제어 메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기할 수 있는 유저 인터페이스 페이지 등
4. `position:fixed`
   - 부모/조상 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 속성 만큼 이동
   - 스크롤을 내리거나 올려도 화면에서 사라지지 않고 항상 같은 곳에 위치



### [추가] emmet

- HTML과 CSS 작성 시, 빠른 마크업을 위해 사용하는 오픈소스
  - 단축키와 약어 등 사용
- [Cheet-Sheet](https://docs.emmet.io/cheat-sheet/)

