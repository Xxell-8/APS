def secret_map(n, arr1, arr2):
    result = []
    for idx in range(n):
        code = bin(arr1[idx] | arr2[idx])[2:].zfill(n)
        decode = code.replace('0', ' ').replace('1', '#')
        result.append(decode)

    return result

print(secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(secret_map(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))