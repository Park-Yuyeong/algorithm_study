function solution(arr) {
    let minValue = Math.min(...arr);
    let answer = arr.filter((i) => i !== minValue);
    
    return answer.length ? answer : [-1];
}
