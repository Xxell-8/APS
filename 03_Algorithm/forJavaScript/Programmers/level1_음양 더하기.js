// 1. forEach 활용
function solution(absolutes, signs) {
    let answer = 0;
    absolutes.forEach((num, idx) => {
        if (signs[idx]) {
            answer += num
        } else {
            answer -= num
        }
    })
    return answer;
}

// 2. reduce 활용
function solution(absolutes, signs) {
    return absolutes.reduce((acc, num, idx) => acc + (num * (signs[idx] ? 1 : -1)), 0);
}