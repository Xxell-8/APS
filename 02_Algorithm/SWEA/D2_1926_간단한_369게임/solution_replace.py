N = 40
result = []

# 1. 1부터 N까지의 수에서
for num in range(1, N+1):
    str_num = str(num)
    # 2. 369를 '-'으로 변환
    clap_num = str_num.replace('3', '-').replace('6', '-').replace('9', '-')

    clap = ''
    # 3-1. '-'가 있으면
    if '-' in clap_num:
        # 3-2. '-'의 개수만큼 clap에 추가
        for char in clap_num:
            if char == '-':
                clap += '-'
        result.append(clap)
    else:
        result.append(clap_num)

print(*result)
