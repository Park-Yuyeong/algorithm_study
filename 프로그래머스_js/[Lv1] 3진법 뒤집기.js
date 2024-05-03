function solution(n) {
    let n3 = '';
    let answer = 0;
    console.log(n.toString(3));
    
    while (n !== 0) {
        n3 += n % 3;
        n = Math.floor(n / 3);
    }

    let l = n3.length;
    
    for (let i = 0; i < l; i++) {
        answer += n3[i] * Math.pow(3, l - i - 1);
    }
    
    return answer;
}
