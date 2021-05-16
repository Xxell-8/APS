import sys
sys.stdin = open('input.txt')


def make_heap(child):
    if child > 1:
        parent = child // 2
        if heap_tree[child] < heap_tree[parent]:
            heap_tree[child], heap_tree[parent] = heap_tree[parent], heap_tree[child]
            make_heap(parent)


def sum_ancestor(node):
    result = 0
    while node > 0:
        node //= 2
        result += heap_tree[node]
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap_tree = [0]
    for num in nums:
        heap_tree.append(num)
        idx = len(heap_tree) - 1
        make_heap(idx)

    print('#{} {}'.format(tc, sum_ancestor(N)))