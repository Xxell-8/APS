def find_multiple(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    if not answer:
        answer.append(-1)
    return answer

print(find_multiple([5, 9, 7, 10], 5))
print(find_multiple([2, 36, 1, 3], 1))
print(find_multiple([3, 2, 6], 10))

# Tip > 단축평가(or)를 활용해서 코드를 좀 더 간결하게 만들 수 있다.
# or 앞에 있는 요소가 False > 뒤를 확인 > 뒤에 있는 요소 반환
# or 앞에 있는 요소가 True > 해당 요소 반환
example1 = [] or [-1]
example2 = [1, 2] or [-1]

print(example1)
print(example2)