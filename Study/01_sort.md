# 1. Sort

> - 대표적인 정렬 방식의 종류는 아래와 같다.
>
> | 알고리즘    | 평균 수행시간 | 기법      | etc.                                |
> | ----------- | ------------- | --------- | ----------------------------------- |
> | 버블 정렬   | O(n²)         | 비교·교환 | 손쉬운 코딩                         |
> | 카운팅 정렬 | O(n+k)        | 비교환    | n이 작을 때만 가능                  |
> | 선택 정렬   | O(n²)         | 비교·교환 | 교환 횟수가 버블·삽입 정렬보다 적음 |
> | 퀵 정렬     | O(nlogn)      | 분할 정복 | 평균적으로 가장 빠름                |
> | 삽입 정렬   | O(n²)         | 비교·교환 | n이 작을 때 효과적                  |
> | 병합 정렬   | O(nlogn)      | 분할 정복 | 연결리스트의 경우 가장 효율적       |
>
> 



## 1. 버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- 시간복잡도: O(n²) 

- 버블 정렬을 활용해서 오름차순을 해보면 아래와 같이 구현

  ```python
  def bubble_sort(a):
      for i in range(len(a)-1, 0, -1):
          for j in range(0, i):
              if a[j] > a[j+1]:
                  a[j], a[j+1] = a[j+1], a[j]
  ```



## 2. 카운팅 정렬(Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
  - 정수로 표현할 수 있는 자료에 대해서만 적용 가능
  - 자료의 범위를 알고 있을 때 사용

- 시간복잡도: O(n+k)
  - n은 리스트 길이, k는 정수의 최댓값



- data = [0, 4, 1, 3, 1, 2, 4, 1]

  - count =[0] * 5 # max(arr) + 1
    - count = [1, 3, 1, 1, 2]
    - 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 count의 원소를 조정(누적 합)
      - count = [1, 4, 5, 6, 8]
    - data를 뒤에서부터 읽고 count[num]을 감소시키면서 temp에 num을 삽입
      - temp = [0, 1, 1, 1, 2, 3, 4, 4]
  - cf. 동일한 값이 여러 개 있을 때 순서를 지키도록(stable sort를 위해서) 뒤에서부터 정렬

  ```python
  # a는 입력 배열, b는 정렬 배열, k는 최댓값
  # c는 카운트 배열
  def counting_sort(a, b, k):
      c = [0] * k
      
      for i in range(0, len(b)):
          c[a[i]] += 1
          
      for i in range(1, len(c)):
          c[i] += c[i-1]
          
      for i in range(len(b)-1, -1, -1):
          b[c[a[i]]-1] = a[i]
          c[a[i]] -= 1
  ```

  

## 3. 선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환

  - 셀렉션 알고리즘을 전체 자료에 적용

- 과정

  - 주어진 리스트 중에서 최소값을 선택
  - 그 값을 리스트 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

- 시간 복잡도: O(n²)

  ```python
  def selection_sort(arr):
      for i in range(len(arr)-1):
          min_idx = i
          for j in range(i+1, len(arr)):
              if arr[min_idx] > arr[j]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
  ```



#### + Selection Algorithm

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘

- 과정

  - 정렬 알고리즘을 이용하여 자료 정렬
    - 최소값 idx를 찾아서 앞으로 보내는 방식
  - 원하는 순서에 있는 원소 가져오기

  ```python
  def select(arr, k):
      for i in range(k):
          min_idx = i
          for j in range(i+1, len(arr)):
              if arr[min_idx] > arr[j]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
      return arr[k-1]
  ```




## 4. 퀵 정렬(Quick Sort)

- 주어진 배열을 두 개로 분할하고, 각각을 정렬
  - 합병정렬과 다른 점은,
    - 합병정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할 시 기준 아이템을 중심으로 이보다 작은 것은 왼쪽, 큰 것은 오른쪽에 위치
    - 정렬 이후, 합병 정렬은 합병이라는 후처리 작업이 필요하나 퀵 정렬은 불필요

- 수행 과정
  - arr = [{69, 10, 30, 2, 16, 8, 31, 22}]
    - pivot = 2, L = 69, R = 22
    - L이 오른쪽으로 이동하며 pivot보다 크거나 같은 원소를 찾고
    - R은 왼쪽으로 이동하며  pivot보다 작은 원소를 찾는다
    - L과 R이 만나 원소 69를 피봇과 교환하여 원소 2의 위치를 확정
  - arr = [**2**, {10, 30, 69, 16, 8, 31, 22}]
    - pivot = 16, L = 10, R = 22
    - L이 찾은 30과 R이 찾은 8을 서로 교환
    - arr = [**2**, {10, *8*, 69, 16, *30*, 31, 22}]
      - L = 8, R = 30
      - L과 R이 만나 원소 69를 피봇과 교환하여 원소16의 위치 확정
        - 위치가 확정되면 해당 원소를 기준으로 집합 나누기
  - arr = [**2**, {10, 8}, 16, {69, 30, 31, 22}]
  - 남은 집합에 대해 같은 과정 반복

- 시간 복잡도: O(nlogn)  ➕ 최악의 경우 O(n²)



#### + 퀵 정렬 알고리즘

```python
def quick_sort(arr, start, end):
    if begin < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)
        
# Hoare partition
def partition(a, start, end):
    pivot = (start + end) // 2
    l = start
    r = end
    
    while l < r:
        while (arr[l] < arr[pivot] and l < r):
            l += 1
        while (arr[r] >= arr[pivot] and l < r):
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            arr[l], arr[r] = arr[r], arr[l]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    return r
```



## 5. 병합정렬(Merge Sort)

- 리스트의 요소를 개별로 나눠서 순서대로 병합하는 방식

```python
def merge_sort(arr):
    n = len(arr)
    # base case
    if n < 2:
        return arr
    
    mid_idx = n // 2
    left = arr[:mid_idx]
    right = arr[mid_idx:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        if sorted_left[l] < sorted_right[r]:
            merged_append(sorted_left[l])
            l += 1
        else:
            merged_append(sorted_right[r])
            r += 1
            
    merged += sorted_left[l:]
    merged += sorted_right[r:]
    
    return merged

    # while l < len(sorted_left):
    #    merged_append(sorted_left[l])
    #    l += 1
    # while r < len(sorted_right):
    #    merged_append(sorted_right[r])
    #    r += 1
```

