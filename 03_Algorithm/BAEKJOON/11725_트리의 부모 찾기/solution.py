import sys
sys.stdin = open('input.txt')

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0 for _ in range(n+1)]

stack = [1]
while stack:
    node = stack.pop()
    for edge in tree[node]:
        if not result[edge]:
            result[edge] = node
            stack.append(edge)
            tree[edge].remove(node)

for i in range(2, n+1):
    print(result[i])