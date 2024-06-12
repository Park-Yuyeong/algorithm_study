function solution(A,B){
    let sortedA = A.sort((a, b) => a - b);
    let sortedB = B.sort((a, b) => b - a);
    let answer = 0;

    for (let i = 0; i < A.length; i++) {
        answer += sortedA[i] * sortedB[i]
    }

    return answer;
}
