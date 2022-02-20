import sys
sys.stdin = open('input.txt')


# 3-1. 전위순회 함수 생성
def preorder(node):
    result[0].append(node)
    for edge in tree[node]:
        if edge != '.':
            preorder(edge)


# 3-2. 중위순회 함수 생성
def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    result[1].append(node)
    if tree[node][1] != '.':
        inorder(tree[node][1])


# 3-3. 후위순회 함수 생성
def postorder(node):
    for edge in tree[node]:
        if edge != '.':
            postorder(edge)
    result[2].append(node)


n = int(input())
# 1. node 번호 대신 알파벳 사용 > dict로 tree 구성
tree = {}
for _ in range(n):
    info = input().split()
    node = info[0]
    tree[node] = tree.get(node, []) + info[1:]

# 2. 결과 값 담을 result 변수 초기화
result = [[] for _ in range(3)]

preorder('A')
inorder('A')
postorder('A')

for answer in result:
    print(''.join(answer))