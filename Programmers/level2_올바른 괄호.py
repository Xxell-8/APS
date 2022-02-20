def bracket(s):
    check = []

    for char in s:
        if char == '(':
            check.append(char)
        else:
            if check:
                check.pop()
            else:
                return False

    return len(check) == 0


print(bracket('()()'))
print(bracket('(())()'))
print(bracket(')()('))
print(bracket('(()('))