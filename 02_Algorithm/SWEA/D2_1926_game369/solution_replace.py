N = 40
result = []

for num in range(1, N+1):
    str_num = str(num)
    clap_num = str_num.replace('3', '-').replace('6', '-').replace('9', '-')
    clap = ''
    if '-' in clap_num:
        for char in clap_num:
            if char == '-':
                clap += '-'
        result.append(clap)
    else:
        result.append(clap_num)

print(*result)
