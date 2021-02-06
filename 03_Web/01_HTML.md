# HTML

> - Hyper Text Markup Language
> - 웹 페이지를 작성하기 위해 웹 콘텐츠의 의미와 구조를 정의하는 언어



## 0. Intro

- Web Standard

  - 월드 와이드 웹(WWW)을 구현하기 위해 따라야 할 표준 또는 규격
  - W3C(HTML5)과  **WHATWG**(HTML Living Standard)가 HTML 표준을 제정

  - [[NEWS] W3C와 WHATWG가 HTML과 DOM 규격을 단일 버전으로 개발하는 데 협력하는 합의안에 서명](https://www.w3.org/blog/2019/05/w3c-and-whatwg-to-work-together-to-advance-the-open-web-platform/)

  

- HTML 이란?
  - Hyper Text
    - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
    - `http`, `html`
  - Markup Language
    - 특정 텍스트에 역할을 부여
    - ex. `h1` 태그를 붙여 의미론적으로 제목임을 마킹하는 것



## 1. 기본 구조

- DOM (Document Object Model)

  - 문서의 구조화된 표현을 제공

    - 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공 

      👉 문서 구조, 스타일, 내용 등을 변경할 수 있도록 돕는 것

  - 웹 페이지의 객체 지향 표현

    - 동일한 문서를 표현·저장·조작하는 방법을 제공



- 기본 구조

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Document</title>
  </head>
  <body>
    
  </body>
  </html>
  ```

  - `<html>` : HTML 문서의 최상위 요소로, 문서의 root를 의미
  - `<head>` : 문서 제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담는 부분으로, 브라우저에 나타나지 않음
  - `<body>` : 브라우저 화면에 나타나는 정보로, 실제 내용에 해당되는 부분



- 요소 (Element)
  - HTML 요소는 시작 태그와 종료 태그, 그 사이에 위치한 콘텐츠(내용)로 구성
  - 태그는 콘텐츠(내용)를 감싸서 그 정보의 성격과 의미를 정의
    - ex. `<h1>contents</h1>`
  - 콘텐츠(내용)이 없는 태그들도 존재
    - `<br>`, `<hr>`, `<img>`, `<input>`, `<link>`, `<meta>`
  - 요소는 중첩(nested) 가능
    - HTML은 오류 없이 레이아웃이 깨져버리기 때문에 어떤 면에서는 오류 정보를 알려주는 프로그래밍보다 디버깅이 어려울 수 있음



- 속성 (Attribute)
  - 속성은 태그의 부가적인 정보
    - 요소에 실제론 나타내고 싶지 않지만 추가적인 내용(이미지 파일의 경로, 크기 등)을 담고 싶을 때 사용
    - 요소의 시작 태그에 위치해야 하며 **이름**과 **값**의 쌍
      - ex.  `<a href="https://www.mozilla.org/">Mozilla</a>`
    - 태그와 상관없이 사용 가능한 속성들(HTML Global Attribute)도 존재



## 2. 시맨틱 태그

> - 의미론적 요소를 담은 태그 (HTML5)
> - 단순히 구역을 나누는 것에서 나아가, '의미'를 가지는 태그를 활용
> - [[참고] Semantics](https://developer.mozilla.org/ko/docs/Glossary/Semantics)



- 의미론적 마크업의 장점
  - 가독성 향상
    - 개발자가 의도한 요소의 의미가 명확히 드러나며,
    - 높은 가독성으로 전반적인 유지·보수에 도움
  - 접근성 향상
    - 검색엔진최적화(SEO)
      - 검색 엔진은 HTML 코드를 읽는데, 시맨틱 태그를 통해 마크업을 하면 콘텐츠의 이해도가 향상
      - 시각장애인을 위한 스크린리더 등 다양한 보조기술 향상에도 도움이 되며, 사용자 경험을 더 좋게 할 수 있음
- Semantic Tag
  - header: 문서 전체나 섹션의 헤더(머릿말)
  - nav: 내비게이션
  - aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section: 문서의 일반적인 구분, 콘텐츠의 그룹을 표현
  - article: 문서, 페이지, 사이트 안에 독립적으로 구분
  - footer: 문서 전체나 섹션의 푸터(마지막 부분)

- Non-Semantic Tag
  - div, span 등



- **시맨틱 웹**
  - 웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여
  - 기존의 단순한 데이터 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축하고자 하는 발상



## 3. HTML 문서 구조화

- 인라인 / 블록 요소
  - 블록 요소(div)는 하나의 태그 요소가 전체를 차지
  - 인라인 요소(span)는 자기 자신의 콘텐츠만큼만 공간을 차지



- 그룹 콘텐츠
  - `<p>`
  - `<hr>` (헤드라인)
  - `<ol>` (순서가 있는 목록), `<ul>` (순서가 없는 목록)
  - `<div>`



- 텍스트 관련 요소
  - `<a>`
  - `<b>`(bold) vs `<strong>`
    - 둘 다 볼드체를 만드는 기능인데, b는 그냥 굵게 / strong은 굵게 + 의미 강조(시맨틱 요소)
    - 스크린 리더가 읽을 때 strong을 강조해서 읽는다
  - `<i>` vs `<em>`
    - 기울임체도 마찬가지로 em은 의미를 부여
  - `<span>`, `<br>`(줄바꿈), `<img>`




- table

  - `<tr>`(열), `<td>`(데이터), `<th>`(헤드)
  - `<thead>`, `<tbody>`, `<tfoot>`
  - `<caption>`
  - 셀 병합 속성: `<colspan>`, `<rowspan>`
  - scope 속성
  - `<col>`, `<colgroup>`

  

- form 

  - `<form>`은 서버에서 처리될 데이터를 제공하는 역할
  - `<form>`의 기본 속성
    - action
    - method

  

- input

  - 다양한 타입을 가지는 입력 데이터 필드
  - `<label>`: 서식 입력 요소의 캡션
  - `<input>` 요소의 동작은 type에 따라 달라짐
    - [[참고] input 유형](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)
  - 공통 속성: name, placeholder, required, autofocus