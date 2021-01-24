# 02. Container

> 여러 개의 값을 저장할 수 있는 객체
>
> - Sequence - 순서가 있는 객체
> - Non-seqeunce - 순서가 없는 객체

## 1. Sequence Container

> `Sequence`는 데이터가 순서대로 나열된 형식이며, 특정 위치 지정 가능
>
> - `list`, `tuple`, `range`, `string`, `binary` 등이 있다.

#### 1. 리스트 (`list`)

- 리스트는 `[]`, `list()`를 통해 생성

- 값에 대한 접근은 indexing, 즉 `list[idx]`를 통해 가능

- 변경가능한(mutable) 객체

  ```python
  fruits = ['apple', 'banana', 'orange']
  print(fruits[0]) 👉 'apple'
  ```

  

#### 2. 튜플 (`tuple`)

- 튜플은 `()`로 묶어서 표현
- 변경이 불가능한(immutable) 객체로, 읽을 수만 있음
  - 불변 객체이기 때문에, '값을 정확히 할당할 수 있다'는 것을 보장

- 직접 사용하기보다는 파이썬 내부에서 다양한 용도로 활용됨

  ```python
  # cf. 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 생성
  single_tuple = ('hello', )
  ```



#### 3. 레인지 (`range()`)

- `range`는 숫자의 시퀀스를 나타내기 위해 사용

  - `range(start, end, step)` : start부터 (end-1)까지 +step만큼 증가
    - start의 기본 값은 0, step의 기본 값은 1

  ```python
  # end 값만 입력한 기본형
  list(range(3))
   👉 [0, 1, 2]
  
  # 범위를 지정한 range
  list(range(5, 9))
   👉 [5, 6, 7, 8]
  
  # step을 활용해 다양한 배열 생성 가능
  ## 점점 작아지는 숫자 배열
  list(range(0, -5, -1))
   👉 [0, -1, -2, -3, -4]
  
  ## 1~10의 숫자 중 홀수만 담은 배열
  list(range(1, 11, 2))
   👉 [1, 3, 5, 7, 9]
  ```

  

#### + Sequence Operation

| operation      | 설명                    |
| -------------- | ----------------------- |
| x `in` s       | containment test        |
| x `not in` s   | containment test        |
| s1 `+` s2      | concatenation           |
| s `*` n        | n번만큼 반복하여 더하기 |
| `s[i]`         | indexing                |
| `s[i:j]`       | slicing                 |
| `s[i:j:k`]     | k간격으로 slicing       |
| len(s)         | 길이                    |
| min(s), max(s) | 최솟값, 최댓값          |
| s.count(x)     | x의 개수                |


## 2. Non-sequence Container

> `Non-sequence`는 데이터에 순서가 없는 형식
>
> - `set`, `dictionary` 등이 있다.



#### 1. 셋 (`set`)

- `set`은 `{}`, `set()`을 통해 생성하며, **중복된 값이 없음**

  - `set`을 활용하면 `list`의 중복된 값 제거 가능

  ```python
  # set은 집합과 동일하게 처리
  set_a = {2, 3, 5}
  set_b = {3, 6, 9}
  
  # 합집합
  print(set_a | set_b) 👉 {2, 3, 5, 6, 9}
  
  # 교집합
  print(set_a & set_b) 👉 {3}
  
  # 차집합
  print(set_a - set_b) 👉 {2, 5}
  ```

  

#### 2. 딕셔너리 (`dict`)

- `dictionary`는 `{}`, `dict()` 를 통해 생성

- 값에 대한 접근은 key (`dict[key]`)를 통해 가능

- `key`와 `value`가 쌍으로 이뤄진 궁극의 자료구조

  - `key`는 **변경 불가능(immutable)한 데이터**만 가능하며, **중복 불가능**
    - immutable : string, integer, float, boolean, tuple, range
  - `value`는 `list`, `dictionary`를 포함한 모든 것이 가능

  ```python
  # 딕셔너리 생성 방법
  dict1 = {'pepper': 5, 'kanda': 3}
  dict2 = dict(pepper=5, kanda=3)
  dict3 = dict()
  dict3['pepper'] = 5
  dict3['kanda'] = 3
  
  # 딕셔너리 메소드
  dict1.keys() 👉 dict_keys(['pepper', 'kanda'])
  dict1.values() 👉 dict_values([5, 3])
  dict1.items() 👉 dict_items([('pepper', 5), ('kanda', 3)])
  ```

  