# [Level 1] 두 개 뽑아서 더하기

- 문제 출처: [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/68644)



- **문제 설명**
  - 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.



- **제한사항**
  - numbers의 길이는 2 이상 100 이하입니다.
  - numbers의 모든 수는 0 이상 100 이하입니다.



- **입출력 예**

| **numbers** | **result**    |
| ----------- | ------------- |
| [2,1,3,4,1] | [2,3,4,5,6,7] |
| [5,0,2,7]   | [2,5,7,9,12]  |



------

- 문제 풀이

  ```python
  def random_sum(numbers):
      answer = []
      for i in range(len(numbers)):
          x = numbers[i]
          for y in numbers[i+1:]:
              plus = x + y
              answer.append(plus)
  
      return sorted(set(answer))
  ```

  

- 풀이 과정

  1. numbers 배열에서 서로 다른 인덱스에 위치한 두 개의 수를 각각 x, y로 설정

  2. for 반복문 안에서 인덱스 순서대로 모든 경우의 수를 새로운 리스트 answer에 추가

       ex) numbers = [1, 2, 3, 4]일 경우,

     ​        plus는 1+2, 1+3, 1+4, 2+3, 2+4, 3+4 순

  3. answer의 중복 요소를 제거하고 sort 처리해서 return