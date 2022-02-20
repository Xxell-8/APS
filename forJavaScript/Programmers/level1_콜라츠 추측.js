function solution(num) {
  let answer = 0;
  while (num != 1 & answer < 500) {
    num % 2 ? num = num * 3 + 1 : num /= 2
    answer += 1
  }
  return answer===500 ? -1 : answer;
}