function charChange(s, n) {
    if (s === ' ') return ' ';
    
    let char = s.charCodeAt();
    
    if (char <= 90) { // uppercase
        return (char + n) <= 90 ? String.fromCharCode(char + n) : String.fromCharCode(char + n - 26);
    } else { // lowercase
        return (char + n) <= 122 ? String.fromCharCode(char + n) : String.fromCharCode(char + n - 26);
    }
}

function solution(s, n) {
    let s_arr = s.split('');
    let answer = s_arr.map((i) => charChange(i, n));
    
    return answer.join('');
}
