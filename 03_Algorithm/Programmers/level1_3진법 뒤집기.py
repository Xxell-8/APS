def ternary_reverse(n):
    # 1. 3진법 변환 함수 생성
    def ternary_scale(n):
        q, r = divmod(n, 3)
        if q == 0:
            return str(r)
        else:
            return ternary_scale(q) + str(r)

    # 2-1. 3진법 변환 후 앞뒤로 뒤집고
    answer = ternary_scale(n)[::-1]
    # 2-2. 10진수로 변환
    return int(answer, 3)


print(ternary_reverse(45))
print(ternary_reverse(125))