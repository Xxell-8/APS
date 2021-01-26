# 06. Data Structure

> 데이터 구조란, 데이터에 편리하게 접근하고, 변경하기 위해 데이터를 저장하거나 조작하는 방법을 말한다.
>
> - **순서가 있는(ordered)** 데이터 구조
>   - 문자열(string)
>   - 리스트(list)
> - **순서가 없는(unordered)** 데이터 구조
>   - 세트(Set)
>   - 딕셔너리(Dictionary)



## 1. String

- 변경 불가능 (immutable)
- 순서가 있고 (ordered)
- 순회 가능 (iterable)



####  1. 탐색

- `str.find(x)`
  - x의 첫 번째 위치를 반환
  - 만약, **x가 없으면 `-1`을 반환**

- `str.index(x)`

  - x의 첫 번째 위치를 반환
  - 만약, **x가 없으면 `Error`**

  ```python
  s = 'apple'
  
  s.find('a') 👉 0
  s.index('a') 👉 0
  
  s.find('f') 👉 -1
  s.index('f') 👉 Value Error
  ```

  

####  2. 변경

- `str.replace(old, new[, count])`

  - 변경할 글자(old)를 새로운 글자(new)로 바꾼 복사본을 반환
  - count를 지정하면 해당 갯수만큼만 시행

  ```python
  s  = 'zoo!gogo!'
  
  s.replace('o', '') 👉 'z!gg!'
  s.replace('o', '', 2) 👉 'z!gogo!'
  ```

  

- `str.strip([chars])`
  - 특정한 문자들을 지정하면,  양쪽 끝의 특정 문자를 제거한 복사본을 반환
    - 왼쪽을 제거 (`lstrip`), 오른쪽을 제거 (`rstrip`)
  - 지정하지 않으면 `공백 문자`를 제거



- `str.split(sep)`

  - 문자열을 특정한 단위(sep)로 나누어 리스트로 반환
  - 지정하지 않으면 `공백 문자`를 기준

  ```python
  data = '5,Tom,01012345678'
  data.split(',') 👉 ['5', 'Tom', '01012345678']
  ```

  

- `'separator'.join(iterable)`

  - separator를 구분자로 사용하여 iterable의 요소들을 이어 붙인문자열을 반환

  ```python
  words = ['Pepper', 'Kanda', 'Cell']
  '+'.join(words) 👉 'Pepper+Kanda+Cell'
  ```

  

- `str.zfill(n)`
  - 왼쪽에 `'0'`을 채워 길이가 n인 문자열의 복사본을 반환
  - n이 len(str)보다 작거나 같으면 원래 문자열을 반환

- `str.rjust(n[, fillchar])`, `str.ljust(n[, fillchar])`

  - 오른쪽(왼쪽)으로 정렬된 문자열을 지정된 fillchar를 사용하여 길이 n인 문자열로 반환 (기본값은 space)
  - n이 len(str)보다 작거나 같으면 원래 문자열을 반환

  ```python
  s = '123'
  
  s.zfill(5) 👉 '00123'
  s.rjust(5, '*') 👉 '**123'
  s.ljust(5, '*') 👉 '123**'
  ```

  

## 2. List

- 변경 가능(mutable)
- 순서가 있고(ordered)
- 순회 가능(iterable)



#### 1. 값 추가/삭제

- `list.append(x)`

  - list의 끝에 x를 추가

- `list.extend(iterable)`

  - list의 끝에 iterable의 모든 항목을 덧붙여서 확장
    - [주의] string의 개별 요소를 하나씩 다 추가

- `list.insert(idx, x)`

  - 정해진 위치 (`idx`)에 x를 추가

  ```python
  animals = ['dog']
  
  a = animals.append('cow')
  print(a) 👉 ['dog', 'cow']
  e = animals.extend(['pig', 'tiger'])
  print(e) 👉 ['dog', 'pig', 'tiger']
  i = animals.insert(1, 'cat')
  print(i) 👉 ['dog', 'cat']
      
  # 맨 끝에 insert하려면 아래와 같이 써야 함
  animals.insert(len(animals), 'end')
  animals.insert(20000, 'end')
  ```

  

- `list.remove(x)`

  - list에서 값이 x인 것을 삭제

- `list.pop(idx)`

  - 정해진 위치 idx에 있는 값을 삭제하고, 그 값을 반환
  - idx가 지정되지 않으면 **마지막 항목**을 삭제하고 반환

- `list.clear()`

  - list의 모든 항목을 삭제



#### 2. 탐색/정렬

- `list.index(x)`
  - list 내에서 x를 찾아 해당 index 값을 반환
- `list.count(x)`
  - list 내에서 x의 개수를 확인
- `list.sort()`
  - list를 정렬
  - 내장함수 `sorted()`와 달리, **원본 list를 변형**하고` None`을 리턴
- `list.reverse()`
  - list를 반대로 뒤집는다



#### 3. 복사

- 아래와 같이 list를 새로운 list에 할당해 복사를 할 경우, 

  - 두 개의 list가  같은 id를 바라보기 때문에 하나를 수정하면 두 개 다 수정

  ```python
  original_list = [1, 2, 3]
  copy_list = original_list
  copy_list[0] = '바꾼다'
  print(copy_list, original_list)
   👉 ['바꾼다', 2, 3] ['바꾼다', 2, 3]
  ```

- `shallow copy`

  - slice 연산자 사용 `[:]`

    ```python
    a = [1, 2, 3, 4]
    # 전체를 똑같이 잘라냄
    b = a[:]
    b[0] = 100
    print(a, b)
     👉 [1, 2, 3, 4]
    	[100, 2, 3, 4]
    ```

  - `list()` 활용

    ```python
    a = [1, 2, 3, 4]
    # list를 새로운 list로 형 변환
    b = list(a)
    b[0] = 100
    print(a, b)
     👉 [1, 2, 3, 4]
    	[100, 2, 3, 4]
    ```

- `deep copy`

  - 만약 중첩된 상황에서 복사를 하려면 깊은 복사를 활용
    - 내부의 모든 객체가 새롭게 값이 변경

  ```python
  import copy
  
  a = [[1, 2, 3], 2, 3]
  b = copy.deepcopy(a)
  b[0][0] = '주소'
  b[1] = '원소'
  
  print(a, b)
   👉 [[1, 2, 3], 2, 3]
      [['주소', 2, 3], '원소', 3]
  ```



#### 4. List Comprehension

- List Comprehension은 표현식과 제어문, 조건문을 통해 리스트를 생성 👉 여러 줄의 코드를 한줄로 단축 가능

  ```python
  [expression for 변수 in iterable if 조건식]
  [expression if 조건식 else 식 for 변수 in iterable]
  ```

  

- List Comprehension의 특징
  
  1. 간결함
  
  2. 성능(일반화의 오류), 최적화
  
     - 성능은 파이썬 자체의 변화와 코드 최적화에 따라 얼마든지 달라질 수 있다.
     - 최신 파이썬 버전은, 일반 loop문에도 비약적인 성능 향상이 있었다.
     - 물론, 일부 코드에서는 컴프리헨션이 여전히 빠르고 map보다도 빠르다
     - 다만 다른 함수나 내장함수를 적용하는 경우는 map이 더 빠름
     - 결론은, 성능이란 누가 더 빠르거나 좋다고 일반화할 수 없다.
  
     "List Comprehension을 남용하면 안 된다"
  
     - 특별한 이유없이 복잡하고 교묘하게 작성하는 것은 나쁜 기술이며 좋은 개발자라 할 수 없다
     - 중첩이 깊은 경우는 억지로 줄이는 것이 더 이해하기 어렵게 만듦
     - **코드의 가독성** >>>>> 간결함
  
  3. 표현력(Pythonic한 표현)



## 3. Set

- 변경 가능(mutable)
- 순서가 없고(unordered)
- 순회 가능(iterable)



- `set.add(elem)`
  - set에 elem을 추가
- `set.update(*others)`
  - set에 iterable의 모든 항목을 추가
- `set.remove(elem)`
  - set에서 elem을 삭제
  - 만약 elem이 없으면 `KeyError`
- `set.discard(elem)`
  - set에서 elem을 삭제
  - elem이 없어도 Error는 발생하지 않음
- `set.pop()`
  - set의 **임의의 원소**를 제거해 반환
  - 순서가 없은 데이터 구조는 hash table을 거쳐서 메모리에 할당되는데, 같은 구조로 계속 만들고 그래서 같은 게 계속 빠지는 것처럼 보인다 > hash table은 파이썬이 종료될 때까지 유지



## 4. Dictionary

- 변경 가능(mutable)
- 순서가 없고(unordered)
- 순회 가능(iterable)



#### 1. 조회

- `dict.get(key[,default])`
  - key를 통해 value를 반환
  - dict에 해당 key가 없어도 `KeyError`가 발생하지 않음
    - default 값을 지정할 수도 있음



#### 2. 추가 및 삭제

- `dict.pop(key[,default])`
  - dict에 key가 있으면 제거
  - key가 없으면 default를 반환 
    - default가 없으면 KeyError



- `dict.update()`

  - 값을 제공하는 key, value로 업데이트

  ```python
  my_home = {'pepper': 5, 'kanda': 3, 'cell': 27}
  
  my_home.update({'pepper': '고양이'})
  my_home.update(cell='주인')
  
  print(my_home)
   👉 {'pepper': '고양이', 'kanda': 3, 'cell': '주인'}
  ```



#### + 딕셔너리 접근 

- `dict.keys()`
- `dict.values()`
- `dict.items()`



## + Built-in Function

> 순회 가능한(iterable) 데이터 구조에 적용가능한 Built-in Function
>
> - map()
> - filter()
> - zip()
> - reduce()



- `map(function, iterable ...)`
  - iterable의 모든 요소에 function을 적용한 후 그 결과를 반환
  - return 값은 **map_object** 형태
  - custom 함수를 적용할 때 유용하게 사용



- `filter(function, iterable)`
  - iterable에서 function 반환된 결과가 True인 것들로 구성해 반환
  - return 값은 **filter_object** 형태



- `zip(*iterables)`
  - 복수의 iterable를 모아서 반환
  - return 값은 `tuple`로 구성된 **zip_object** 형태

