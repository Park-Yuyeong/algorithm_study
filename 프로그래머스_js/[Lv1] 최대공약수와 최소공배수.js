function solution(n, m) {
    let answer = [0, 0];
    let x = Math.min(n, m);
    
    for (let i = x; i > 0; i--) {
        if (!(n % i || m % i)) {
            answer[0] = i;
            break;
        }
    } // 최대공약수
    
    answer[1] = n * m / answer[0]; // 최소공배수
    return answer;
}
