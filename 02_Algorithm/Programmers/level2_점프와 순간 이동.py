# KEY > 순간이동으로 이동할 수 없는 구간(홀수) 구하기
# 1. 직접 계산
def iron_suit(n):
    jump = 0
    while n != 0:
        if n % 2:
            n = (n-1) / 2
            jump += 1
        else:
            n /= 2
    return jump

# 2. 이진수 활용
def iron_suit_bin(n):
    return bin(n).count('1')

print(iron_suit(5))
print(iron_suit(6))
print(iron_suit(5000))

print(iron_suit_bin(5))
print(iron_suit_bin(6))
print(iron_suit_bin(5000))