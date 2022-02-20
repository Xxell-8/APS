# [Level 1] 핸드폰 번호 가리기

- 문제 출처: [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/12948)



- **문제 설명**
  - 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
  - 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.



- **제한 조건**
  - s는 길이 4 이상, 20이하인 문자열입니다.



- **입출력 예**

  | **phone_number** | **return**    |
  | ---------------- | ------------- |
  | '01033334444'    | '*******4444' |
  | '027778888'      | '*****8888'   |



----

- 문제 풀이

  ```python
  def hidden_nums(phone_number):
      # 뒷 4자리를 slicing해서 우측 정렬하고
      ## phone_number 길이만큼 '*' 채우기
      return phone_number[-4:].rjust(len(phone_number), '*')
  ```



- 추가 개념 정리_ 정해진 길이(n)만큼 문자열(text) 늘리는 방법

   ① text**.zfill(n)**

    \- text 길이가 n이 될 때까지 왼쪽에 0 채우기

    ex. '123'.**zfill**(5) 👉 '00123' 



​		 ② text.**rjust(n, @)** & text.**ljust(n, @)**

  		- text를 R(or L)로 정렬하고, 길이가 n이 될 때까지 @ 채우기

  		ex. '123'.**rjust**(5, '*') 👉 '**123' 

​        		'123'.**ㅣjust**(5, '*') 👉 '123**' 