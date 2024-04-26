function solution(n) {
    let nn = n + '';
    let arr = nn.split('');
    
    arr.sort((a, b) => b - a);
    
    return parseInt(arr.join(''));
}
