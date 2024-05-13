function solution(s) {
    let answer = [];
    let memo = {};
    
    for (let i = 0; i < s.length; i++){
        memo[s[i]] === undefined ? answer.push(-1) : answer.push(i - memo[s[i]]);
        memo[s[i]] = i;
    }
    return answer;
}
