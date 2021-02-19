# String



## 1. 패턴 매칭

> - Brute Force
> - KMP 알고리즘
> - 보이어-무어 알고리즘



#### 1. Brute force

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

- 시간복잡도: O(MN)

  ```python
  text =  'Simple is better than complex'
  pattern = 'better'
  
  # 1. while 활용
  def brute_force(text, pattern):
      i = 0
      j = 0
      while i < len(text) and j < len(pattern):
          if text[i] != pattern[j]:
              i -= j
              j -= 1
          i += 1
          j += 1
      if j == len(pattern):
          return i - len(pattern)
      else:
          return -1
      
  # 2. for - in 활용
  def brute_force(pattern, text):
      N = len(text)
      M = len(pattern)
      
      for i in range(N-M+1):
          count = 0
          for j in range(M):
              if text[i+j] == pattern[j]:
                  count += 1
              else:
                  break
          if cnt == M:
              return i
      return -1
  ```



#### 2. KMP 알고리즘 (더 찾아보기)

- 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 **전처리**하여 배열 next[M]을 구해서 잘못된 시작을 최소화
  - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
  - 매칭이 실패했을 때 돌아갈 곳을 계산
- 시간 복잡도: O(M+N)



#### 3. 보이어-무어 알고리즘

- 패턴의 오른쪽에서 왼쪽으로 비교

  - 패턴의 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 패턴의 길이만큼 이동

    | s    |  i   | m    | p    | l    |   e   | p    | y    | t    | h    | o    | n    |
    | ---- | :--: | ---- | ---- | ---- | :---: | ---- | ---- | ---- | ---- | ---- | ---- |
    | p    |  y   | t    | h    | o    | **n** |      |      |      |      |      |      |
    |      |      |      |      |      |   👉   | p    | y    | t    | h    | o    | n    |

  - 패턴의 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재할 경우, 해당 문자의 jump만큼 이동

    | p    |  i   | i    | y    | p     |  n   | p    | y    | t    | h     | o    | n    |
    | ---- | :--: | ---- | ---- | ----- | :--: | ---- | ---- | ---- | ----- | ---- | ---- |
    | p    |  y   | t    | h    | **o** |  n   |      |      |      |       |      |      |
    |      |      |      | 👉    | p     |  y   | t    | h    | o    | **n** |      |      |
    |      |      |      |      |       |  👉   | p    | y    | t    | h     | o    | n    |

    - Jump 설정

      |  p   |  y   |  t   |  h   |  o   |  n   |  나머지 문자  |
      | :--: | :--: | :--: | :--: | :--: | :--: | :-----------: |
      |  5   |  4   |  3   |  2   |  1   |  0   | 6 (패턴 길이) |



## 2. 문자열 암호화

#### 1. 시저 암호



#### 2. bit 열 암호화

- 배타적 논리합(exclusive-or) 연산 사용
  - x == y 👉 0, x != y 👉 1



## 3. 문자열 압축

#### 1. Run-length encoding 알고리즘

- 같은 값이 몇 번 반복되는지를 나타내며 압축
  - ABBBBBBBBA 👉 A1B8A1



#### 2. 허프만 코딩 알고리즘 (뭔지 모름..)

