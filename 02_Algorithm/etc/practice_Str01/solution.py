## 문자열 뒤집기 ##


# 1. 거꾸로 담기
def str_reverse1(word):
    result = ''
    for i in range(len(word)-1, -1, -1):
        result += word[i]
    return result


def str_reverse2(word):
    idx = len(word) -1
    result = ''
    while idx >= 0:
        result += word[idx]
        idx -= 1
    return result


# 2. swap 하기
def str_swap(word):
    result = list(word)
    n = len(result) // 2

    for i in range(n):
        result[i], result[-(i+1)] = result[-(i+1)], result[i]
    return ''.join(result)


# 3. 재귀로 풀기
def str_reverse3(word):
    last = len(word) - 1
    if last == 0:
        return word

    return word[last] + str_reverse2(word[:last])


word = 'algorithm'

print(str_reverse1(word))
print(str_swap(word))
print(str_reverse2(word))
print(str_reverse3(word))