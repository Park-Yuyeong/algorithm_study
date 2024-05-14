function solution(a, b, n) {
    let result = 0;

    while (n >= a){
        result += Math.floor(n / a) * b;
        n = (n % a) + Math.floor(n / a) * b;
    }
    return result;
}
