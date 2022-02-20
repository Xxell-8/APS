# Queue



## 1. Queue

> 선입선출(FIFO, First-In First-Out)

#### 1. 자료구조

- 삽입과 삭제의 위치가 제한적인 자료구조
  - 뒤에서 삽입, 앞에서 삭제
- 가장 먼저 저장된 원소 👉 `front`
- 가장 마지막에 저장된 원소 👉 `rear`



#### 2. 연산

- `enQueue(item)` : 자료 IN (뒤에 삽입)
- `deQueue()` : 자료 OUT (맨앞에 자료 삭제+반환)
- `createQueue()` : 공백 상태의 큐 생성
- `isEmpty()` : 공백인지 확인
- `isFull()` : 포화상태인지 확인
- `Qpeek()` : front 요소 반환



#### 3. 큐의 구현

#####  1. 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - 첫 번째 원소의 idx 👉 `front`
  - 마지막 원소의 idx 👉 `rear`

- 상태 표현

  - 초기 상태: front = rear = -1
  - 공백 상태: front = rear
  - 포화 상태: rear = n-1

- 선형큐의 구현

  - 초기 큐 생성

    - 크기 n인 1차원 배열 생성
    - front와 rear를 -1로 초기화

  - 공백/포화 상태 검사

    ```python
    def is_empty():
        return front == rear
    def is_full():
        return front == len(Q) - 1
    ```

  - 삽입

    - 마지막 원소 뒤에 새로운 원소 삽입을 위해
      - rear 값을 하나 증가시켜 새로운 원소 삽입 위치 지정
      - Q[rear]에 item 저장

    ```python
    def enQueue(item):
        global rear
        if is_full():
            print('Queue Full')
        else:
            rear += 1
            Q[rear] = item
    ```

  - 삭제

    - 가장 앞에 있는 원소를 삭제하기 위해
      - front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동

    ```python
    def deQueue():
        if is_empty():
            print('Queue Empty')
        else:
            front += 1
            return Q[front]
    ```

  - 검색

    - 큐의 첫 번째 원소 반환

    ```python
    def Qpeek():
        if is_empty():
            print('Queue Empty')
        else:
            return Q[front + 1]
    ```

- 선형큐의 한계

  - 잘못된 포화 상태 인식
    - 원소의 삽입과 삭제를 계속할 경우, 배열 앞 부분에 공간이 있음에도 포화 상태로 인식할 수 있음



#####  2. 원형 큐

- 1차원 배열을 활용하되, 처음과 끝이 연결된 원형 형태로 가정

  - front와 rear의 위치가 n-1이 된 다음, 다시 처음 인덱스인 0으로 이동
    - 나머지 연산자 `%` 활용

- 원형 큐의 구조

  - 초기 공백 상태: front = rear = 0

- 원형 큐의 구현

  - 초기 공백 큐 생성

    - 크기 n인 1차원 배열 생성
    - front와 rear를 0으로 초기화

  - 공백상태 및 포화상태 검사

    - 공백상태: front = rear
    - 포화상태: 삽입할 rear의 다음 위치 = front
      - (rear + 1) % n = front

    ```python
    def is_empty():
        return front == rear
    
    def is_full():
        return (rear+1) % len(cQ) == front
    ```

  - 삽입

    - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
      - rear 갑을 조정하여 새로운 원소를 삽입할 자리를 마련 
        - rear = (rear + 1) % n
      - 해당 인덱스에 해당하는 배열원소 cQ[rear]에 item 저장

    ```python
    def enQueue(item):
        global rear
        if is_full():
            print('Queue_Full')
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item
    ```

  - 삭제

    - 가장 앞에 있는 원소를 삭제하기 위해
      - front 값을 조정하여 삭제할 자리를 준비
      - 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능

    ```python
    def deQueue():
        global front
        if is_empty():
            print('Queue_empty')
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]
        
    def delete():
        global front
        if is_empty():
            print('Queue_empty')
        else:
            front = (front + 1) % len(cQ)
    ```



##### 3. 연결 큐





#### 연결 큐의 구조

- 단순 연결 리스트(Linked List)를 이용한 큐
  - 큐의 원소: 단순 연결 리스트의 노드
  - 큐의 원소 순서: 노드의 연결 순서 (링크로 연결)
  - front: 첫 노드를 가리키는 링크
  - rear: 마지막 노트를 가리키는 링크
- 상태표현
  - 초기 상태: front = rear = None
  - 공백 상태: front = rear = None



#### 연결 큐의 구현

- 교재 참고



#### 우선순위 큐

- 우선순위 큐의 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO가 아니라 우선순위가 높은 순서대로 먼저 OUT
- 우선순위 큐의 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 태스크 스케쥴링



- 구현
  - 배열을 이용한 우선순위 큐
    - 배열을 이용해 자료 저장
    - 원소 삽입 과정에서 우선순위를 비교하여 적절한 위치에 삽입
    - 가장 앞에 최고 우선순위 원소가 위치
    - BUT, 삽입/삭제 연산이 일어날 때 원소 재배치 발생 > 소요되는 시간이나 메모리 낭비가 클 수 있음
  - 리스트를 이용한 우선순위 큐
- 기본 연산
  - heap



#### 큐의 활용: 버퍼(Buffer)

- 버퍼
  - 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
- 버퍼의 자료 구조
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
  - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용 



-------

##### 마이쮸

```python
# 마이쮸 개수
n = 20

queue = [(1, 0)]

new_people = 1
last_people = 0

while n > 0:
    num, cnt = queue.pop(0)
    last_people = num
    cnt += 1
    
    n -= cnt
    new_people += 1
    
    queue.append((num, cnt))
    queue.append((new_people, 0))
    #print(queue)
    
print(last_people)
```



## BFS(Breadth First Search)

- 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용



##### DFS vs BFS

![image-20210303141923320](etc/05_queue.assets/image-20210303141923320.png)

- **DFS** : A - B - E - F - C - D - G - H - I

- **BFS** : A - B - C - D - E - F - G - H - I



#### BFS 알고리즘

```python
def bfs(graph, start):
    visited = [0] * (n+1)
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        if not visited[current]:
            visited[current] = 1
            
            for edge in graph[current]:
                if not visited[edge]:
                    queue.append(edge)
```



