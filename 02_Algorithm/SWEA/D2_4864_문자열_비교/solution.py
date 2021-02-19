import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 1. input 받기
    pattern = input()
    text = input()

    # 2. text 길이만큼 반복 (Brute force 활용)
    for i in range(len(text)):
        count = 0
        # 3-1. text를 pattern의 길이만큼 반복하면서
        for j in range(len(pattern)-len(pattern)+1):
            # 3-2. 해당 자리가 일치하면 +1
            if text[i+j] == pattern[j]:
                count += 1
            # 3-3. 다르면 break
            else:
                break

        # 3-4. 일치하는 글자가 pattern의 길이와 같으면 +1
        if count == len(pattern):
            result = 1
            break
    else:
        result = 0

    print('#{} {}'.format(tc, result))