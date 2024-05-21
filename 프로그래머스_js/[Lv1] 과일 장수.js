function solution(k, m, score) {
    const sortedScore = score.sort((a, b) => b - a);
    let result = 0;
    
    for (let i = m - 1; i < sortedScore.length; i += m){
        result += sortedScore[i] * m;
    }
    
    return result;
}
