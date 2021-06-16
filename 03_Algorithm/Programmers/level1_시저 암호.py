def caesar_password(s, n):
    result = ''
    for char in s:
        if char.isupper():
            alpha = ((ord(char) - ord('A')) + n) % 26
            result += chr(ord('A') + alpha)
        elif char.islower():
            alpha = ((ord(char) - ord('a')) + n) % 26
            result += chr(ord('a') + alpha)
        else:
            result += ' '

    return result


print(caesar_password('AB', 1))
print(caesar_password('za', 27))
print(caesar_password('a B z', 4))

# Tip > 만약 n이 26 이상으로도 주어진다면, n % 26 추가
