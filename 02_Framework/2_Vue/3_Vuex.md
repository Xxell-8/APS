# 03. Vuex

> - statement management pattern + library for vue.js
>   - 상태 관리 패턴 + 라이브러리
> - 상태를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
>   - state가 예측 가능한 방식으로만 변경될 수 있도록 보장하는 규칙 설정
>   - 애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할
> - Vue의 공식 devtools와 통합되어 기타 고급 기능 제공



## 1. Vuex Core Concept

- **단방향 데이터 흐름**
  - 상태(state)는 앱을 작동하는 원본 소스 (data)
  - 뷰(view)는 상태의 선언적 매핑
  - 액션(action)은 뷰에서 사용자 입력에 대해 반응적으로 상태를 바꾸는 방법(methods)

- 단방향 데이터 흐름의 단점

  - 공통의 상태를 공유하는 여러 컴포넌트가 있는 경우 빠르게 복잡해짐

- 상태 관리 패턴
  - 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리하도록 함
  - 컴포넌트는 커다란 뷰가 되며 모든 컴포넌트는 트리에 상관없이 state에 접근하거나 동작을 트리거할 수 있음
  - 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리함으로써 코드의 구조와 유지 관리 기능 향상



## 2. Vuex 구성 요소

#### 1. State

- 중앙에서 관리하는 모든 상태 정보(data)
- Mutations에 정의된 method에 의해 변경
- 여러 컴포넌트 내부에 있는 특정 state를 중앙에서 관리
  - Vuex Store에서 컴포넌트에서 사용하는 state를 한 눈에 파악 가능
  - state가 변화하면 해당 state를 공유하는 컴포넌트의 DOM은 자동 렌더링
- 컴포넌트는 Vuex Store에서 state 정보를 가져와 사용



#### 2. Actions

- 컴포넌트에서 `dispatch()` 메서드에 의해 호출
- Backend API와 통신하여 Data Fetching 등의 작업을 수행
  - 동기적 작업 뿐만 아니라 **비동기적 작업 포함 가능**
- 항상 `context`가 인자로 넘어옴
  - store.js 파일 내에 있는 모든 요소에 접근해서 속성 접근 + 메서드 호출 가능
  - 단, (가능하지만) state를 직접 변경하지 않음
- mutations에 정의된 메서드를 `commit` 메서드로 호출
- state는 mutations 메서드를 통해서만 조작
  - 명확한 역할 분담을 통해 서비스 규모가 커져도 state를 올바르게 관리하기 위함



#### 3. Mutations

- Actions에서 `commit()` 메서드에 의해 호출
- 비동기적으로 동작하면 state가 변화하는 시점이 달라질 수 있기 때문에 **동기적 코드만 작성**
- mutations에 정의하는 메서드의 첫 번째 인자로 `state`가 넘어옴



#### 4. Getters

- state를 변경하지 않고 활용하여 계산을 수행 (computed와 유사)
  - 실제 계산된 값을 사용하는 것처럼 getters는 저장소의 상태(state)를 기준으로 계산
- getters 자체는 state를 변경하지 않음
  - state를 특정한 조건에 따라 구분(계산)



## 3. 바인딩 헬퍼

- `mapState`, `mapGetters`, `mapActions`, `mapMutations`
- Spread Operator(`...`)를 활용해 각 프로퍼티를 가져와 필요한 부분만 사용

