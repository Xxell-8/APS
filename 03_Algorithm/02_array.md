# 2. Array



## 1. 2차원 배열 생성

```python
n, m = 3, 4 # n은 행의 개수, m은 열의 개수

#1
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#2
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
    
#3
arr = [list(map(int, input().split())) for _ in range(n)]
```





## 2. 2차원 배열 순회

#### 1. 행 우선순회

```python
for col in range(n):
    for row in range(m):
        print(arr[col][row])
        
# 역순회
for col in range(n):
    for row in range(m-1, -1, -1):
        print(arr[col][row])
```



#### 2. 열 우선순회

```python
for row in range(m):
    for col in range(n):
        print(arr[col][row])
        
# 역순회
for row in range(m):
    for col in range(n-1, -1, -1):
        print(arr[col][row])
```



#### 3. 지그재그 순회

```python
#1
for col in range(n):
    for row in range(m):
        print(arr[col][row + ((m-1)-(2*row)) * (col % 2)])
        
#2
for col in range(n):
    if col % 2 == 0:
        for row in range(m):
            print(arr[col][row])
    else:
        for row in range(m-1, -1, -1):
            print(arr[col][row])
```



#### 4. 델타를 이용한 2차원 배열 탐색

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(arr)
m = len(arr[0])
col = 1
row = 1

#상하좌우
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]


for i in range(4):
    nc = col + dc[i]
    nr = row + dr[i]
    
    if 0 <= nc < n and 0 <= nr < m:
        print(arr[nc][nr])
```



#### 5. 전치행렬

```python
for i in range(n):
    for j in range(m):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



## 3. 부분집합

```python
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

#### + 비트 연산 활용

```python
arr = [1, 2, 3, 4]
n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = ' ')
    print()
print()
```

##### ++ 부분집합 구하기

```python
def subset(arr):
    result = []
    for i in range(1 << len(arr)):
        tmp = []
        for j in range(len(arr)):
            if i & (1 << j):
                tmp.append(arr[j])
        result.append(tmp)
    return result
```

- (내 생각) 비트 연산을 사용하는 이유는, `arr`의 길이만큼 0, 1로 구성된 숫자를 만들어서 T/F 판단하는 느낌 ^^ 

- i는 0부터 `2^(len(arr))-1` 의 값을 2진수로 가진다.

  - i는 모든 부분집합의 경우의 수를 2진수로 나타낸 것

    👉 0, 1, 10, 11, 100, 101, 110, 111, ...

- `1 << j`는 2진수에서 원소의 위치를 표시

- [example]

  > arr = [1, 2, 3] 
  >
  > len(arr) = 3   📌비트를 3자리 수로 생각해보자!
  >
  > i 👉 1<<len(arr) 👉 (00)0, (00)1, (0)10, (0)11, 100, 101, 110, 111
  >
  > j 👉 0, 1, 2
  >
  > 1 << j 👉 (00)1, (0)10, 100
  >
  > | i     | j 👉 1 << j 👉 i & (1 << j)                                    | tmp       |
  > | ----- | ------------------------------------------------------------ | --------- |
  > | (00)0 | 0 👉 (00)1 👉 F <br />1 👉 (0)10 👉 F<br />2 👉 100 👉 F           | -         |
  > | (00)1 | 0 👉 (00)1 👉 **T**<br />1 👉 (0)10 👉 F<br />2 👉 100 👉 F        | [1]       |
  > | (0)10 | 0 👉 (00)1 👉 F<br />1 👉 (0)10 👉 **T**<br />2 👉 100 👉 F        | [2]       |
  > | (0)11 | 0 👉 (00)1 👉 **T**<br />1 👉 (0)10 👉 **T**<br />2 👉 100 👉 F    | [1, 2]    |
  > | 100   | 0 👉 (00)1 👉 F<br />1 👉 (0)10 👉 F<br />2 👉 100 👉 **T**        | [3]       |
  > | 101   | 0 👉 (00)1 👉 **T**<br />1 👉 (0)10 👉 F<br />2 👉 100 👉 **T**    | [1, 3]    |
  > | 110   | 0 👉 (00)1 👉 F<br />1 👉 (0)10 👉 **T**<br />2 👉 100 👉 **T**    | [2, 3]    |
  > | 111   | 0 👉 (00)1 👉 **T**<br />1 👉 (0)10 👉 **T**<br />2 👉 100 👉 **T** | [1, 2, 3] |

  



## 4. 검색

#### 1. 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 배열 등 순차구조로 구현된 자료 구조에서 원하는 항목을 찾을 때 유용
  - 알고리즘이 단순하지만, 검색 대상의 수가 많은 경우 수행시간이 급격히 증가하여 비효율적

- 정렬이 된 경우와 되지 않은 경우로 나눌 수 있음

  1. 정렬이 되지 않는 경우

     - 과정
       - 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
       - 키 값과 동일한 원소의 value/index/TF 등을 반환
       - 마지막까지 찾지 못하면 검색 실패
     - 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정
       - 평균 비교 횟수: (n+1) / 2 👉 O(n)

     ```python
     def sequential_search(arr, n, key):
         i = 0
         while i < n and arr[i] != key:
             if i < n and arr[i] == key:
                 return i
             else:
                 return -1
            	i += 1
     ```

     

  2. 정렬이 되어 있는 경우

     - 과정 (오름차순 기준)
       - 자료를 순차적으로 검색하며 키 값을 비교
       - 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 종료
     - 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정
       - 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듬

     ```python
     def sequential_search(arr, n, key):
         i = 0
         while i < n and arr[i] < key:
             if i < n and arr[i] == key:
                 return i
             else:
                 return -1
            	i += 1
     ```

     

#### 2. 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 진행
  - 이진 검색을 순환적으로 반복 수행하여 검색 범위를 반으로 줄어가며 보다 빠르게 검색
  - **정렬되어 있는 경우**에만 활용 가능

- 과정
  - 자료의 중앙에 있는 원소를 선택
  - 중앙원소의 값과 찾고자 하는 목표 값을 비교
  - 목표 값이 중앙 원소의 값보다 작으면 왼쪽 반에 대해 검색, 크다면 오른쪽 반에 대해 검색
  - 목표 값을 찾을 때까지 위의 과정을 반복

```python
def binary_search(arr, key):
    start = 0
    end = len(arr)-1
    
    while start <= end:
        middle = (start+end) // 2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return False
```

##### + 재귀함수

```python
def binary_search(arr, low, high, key):
    if low > high:
        return False
    else:
        middle = (low+high) // 2
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            return binary_search(arr, low, middle-1, key)
        else:
            return binary_search(arr, middle+1, high, key)
```

