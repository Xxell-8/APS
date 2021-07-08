function solution(arr) {
  return arr.reduce((acc, num) => acc + num) / arr.length;
}