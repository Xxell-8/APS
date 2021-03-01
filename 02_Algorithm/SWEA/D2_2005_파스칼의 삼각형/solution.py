import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = [[1]]
    last_row = [0, 1, 0]

    for col in range(1, n):
        nums = []
        left = last_row.pop()
        for row in range(col+1):
            right = last_row.pop()
            nums.append(left+right)
            left = right
        last_row += [0] + nums + [0]
        result.append(nums)

    print('#{}'.format(tc))
    for row in result:
        print(' '.join([str(num) for num in row]))