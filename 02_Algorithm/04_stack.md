# Stack



## 1. Stack

>  후입선출(LIFO, Last-In First-Out)

#### 1. 자료구조

- 자료를 선형으로 저장할 저장소
- Python에서는 list, C 언어에서는 array 활용
- 스택에서 마지막 삽입된 원소의 위치 👉 `top`



#### 2. 연산

- `push` : 자료 IN (삽입)
- `pop`: 자료 OUT(삭제+반환)
- `is_empty`: 스택이 공백인지 확인
- `peek`: top에 있는 요소 반환



```python
class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if len(self.data) else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None
        
    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return None
```



## 2. DP (Dynamic Programming)

#### 1. Memoization

> - Memoization은, 'to put in memory'라는 뜻

- 프로그램을 실행할 때, 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
  - 동적 계획법(DP)의 핵심 기술
  



#### 2. DP(Dynamic Programming)

- 최적화 문제를 해결하는 알고리즘

- 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해를 이용해 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘



#####  [Example] 피보나치 수열

- 재귀 호출에서 발생하는 중복 호출 문제 및 오버 플로우를 개선하기 위해 memoization을 활용할 수 있음
  - 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면, 실행시간은 O(n)으로 줄일 수 있다.

  ```python
  # 1. 재귀함수
  def fibo_recursive(n):
      if n < 2:
          return n
      return fibo(n-1) + fibo(n-2)
  
  # 2. 메모이제이션
  memo = [0, 1]
  def fibo_memoization(n):
      if n >= 2 and len(memo) <= n:
          memo.append(fibo_memoization(n-1) + fibo_memoization(n-2))
      return memo[n]
  
  # 3. 동적계획법
  def fibo_dp(n):
      f = [0, 1]
      for i in range(2, n+1):
          f.append(f[i-1] + f[i-2])
      return f[n]
  ```

  

## 3. DFS (깊이 우선 탐색)

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색

  - 깊이 우선 탐색(DFS)
  - 너비 우선 탐색(BFS)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해가다가 더 이상 갈 곳이 없으면, 가장 마지막에 만난 갈림길 간선이 있는 정점으로 되돌아와 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법

- 가장 마지막에 만난 갈림길의 정점으로 되돌아가 다시 깊이 우선 탐색을 반복

  ​	👉 후입선출 구조의 Stack 활용



#### 1. Graph

- 기본 개념

  ① 정점(Vertex, Node)

  ② 간선(Edge)

  ③ 방향

  - Directed Graph
  - Undirected Graph

- 자료 구조 받기

  ```python
  node = 6
  edge = 5
  edges = [(1, 4), (1, 3), (2, 3), (2, 5), (4, 6)]
  
  # 1. Dictionary (Node 이름이 길거나 복잡할 때)
  line = {
      'A': ['D', 'C'],
      'B': ['C', 'E'],
      'C': [],
      'D': ['F'],
      'E': [],
      'F': []
  }
  
  # 2. Adj List_ 인접 리스트 (Node가 정수일 경우 쓰기) 👉 O(n)
  line = [
      [],
      [4, 3],
      [3, 5],
      [],
      [6],
      [],
      []
  ]
  
  # 3. Adj Matrix_ 인접 행렬 (E가 많고 V가 적을 때) 👉 O(1)
  line = [
      [0, 0, 0, 0, 0, 0, 0],
      [0, F, F, T, T, F, F],
      [0, F, F, T, F, T, F],
      [0, F, F, F, F, F, F],
      [0, F, F, F, F, F, T],
      [0, F, F, F, F, F, F],
      [0, F, F, F, F, F, F]
  ]
  ```



- DFS 알고리즘

  ```python
  def dfs(v, e, graph, s, g):
      visited = [0 for _ in range(v+1)]
      to_visit = [s]
      
      while to_visit:
          current = to_visit.pop()
          if not visited[current]:
              visited[current] = 1
              to_visit += graph[current]
              
      return visited[g]
      
  
  # Node, Edge 갯수
  v, e = map(int, input().split())
  graph = [[] for _ in range(v+1)]
  
  # Edge 정보
  for _ in range(e):
      a, b = map(int, input().split())
      graph[a].append(b)
      # 무방향일 경우, graph[b].append(a) 추가
  
  # 시작점, 종료점 받기
  s, g = map(int, input().split())
  
  print(solution(v, e, graph, s, g))
  ```

  - 최적화 DFS (Start에서 Goal로 가는 경로 존재 여부 확인)

    ```python
    def solution(v, e, graph, s, g):
        visited = [0 for _ in range(v+1)]
        to_visit = [s]
        
        while to_visit:
            current = to_visit.pop()
            if current == g:
                return 1
            
            if not visited[current]:
                visited[current] = 1
                for v in graph[current]:
                    if not visited[v]:
                        to_visit.append(v)
                
        return 0
    ```



## 4. 백트래킹

- 백트래킹 기법은 해를 찾는 도중에 '막히면'(해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다. 
- 백트래킹 기법은 최적화 문제와 결정 문제를 해결할 수 있다.
  - 결정 문제: 문제의 조건을 만족하는 해가 존재하는 지 여부를 답하는 문제
    - 미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합 등
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
- 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다
- 가지치기: 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.



- DFS와의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임
  - DFS는 모든 경로를 추적하는 데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - DFS를 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 DFS를 가하면 당연히 처리 불가능한 문제
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능



- 백트래킹 알고리즘
  - 상태 공간 트리의 깊이 우선 검색을 실시
  - 각 노드가 유망한지 점검
  - 만약 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 계속



## 5. 분할 정복 알고리즘

- 설계 전략
  - 분할: 해결할 문제를 여러 개의 작은 부분으로 나누기
  - 정복: 나눈 작은 문제를 각각 해결
  - 통합: (필요하다면) 해결된 해답을 모으기



#####  [Example] 거듭 제곱

```python
# 반복문을 이용한 선형시간 O(n)
def iterative_power(x, n):
    result = 1
    for i in range(1, n+1):
        result *= x
    return result

# 분할 정복 O(logN)
def recursive_power(base, exponent):
    if base == 0 or exponent == 0:
        return 1
    elif exponent == 1:
        return base

    if exponent % 2 == 0:
        new_base = power(base, exponent//2)
        return new_base ** 2
    else:
        new_base = power(base, (exponent-1) // 2)
        return (new_base ** 2) * base
```



-----

### 부분집합 구하기

- 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합을 powerset이라 하며, 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분 집합의 개수는 2^n이 나온다
- 백트래킹 기법으로  powerset을 구해보다
  - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들때 T/F를 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
  - 여기서 배열의 i 번쨰 항목은 i번째 원소가 부분집합의 값인지 아닌지를 나타내는 값

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N # 해당 원소를 뽑았는지 체크

def powerset(idx):
    if idx == N:
        print(sel)
        #for i in range(N):
            #if sel[i]:
                #print(arr[i], end=' ')
        #print()
        
    else:
        # idx 자리의 원소를 뽑고 간다
        sel[idx] = 1
        powerset(idx+1)
        # idx 자리의 원소를 안뽑고 간다
        sel[idx] = 0
        powerset(idx+1)

powerset(0)
```



순열

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 사용했는지 확인

def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1 # 사용했다는 표시
                perm(idx+1)
                check[i] = 0 # 다음 반복을 위한 원상복구
                
perm(0)
```

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N

def perm(idx, check):
    if idx == N:
        print(sel)
        return
    
    for i in range(N):
        # i 번째 원소를 사용했으면 continue
        if check & (1 << i):
            continue
        sel[idx] = arr[i]
        perm(idx+1, check | (1 << i)) # 일회성이라 원상복구 없어도 됨
      
perm(0, 0)
```

SWAP 방식을 활용한 순열 구하기

```python
N = 3
arr = [1, 2, 3]

def perm(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]
            
perm(0)
```

​    



