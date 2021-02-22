# 1. 홀짝 구분
def middle_letter1(s):
    if len(s) % 2:
        return s[len(s)//2]
    else:
        return s[len(s)//2 - 1 : len(s)//2 + 1]


# 2. 홀짝 구분 없이 처리
def middle_letter2(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]

print(middle_letter1('abcde'))
print(middle_letter1('qwer'))

print(middle_letter2('abcde'))
print(middle_letter2('qwer'))
