function solution(num) {
    let count = 0;
    
    while (num !== 1 && count < 500) {
        num = num % 2 ? num * 3 + 1 : num / 2;
        
        count++;
    }
    
    return num === 1 ? count : -1
}
