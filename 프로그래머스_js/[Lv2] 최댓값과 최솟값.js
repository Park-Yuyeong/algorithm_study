function solution(s) {
    const s_arr = s.split(' ').map(Number);
    return Math.min(...s_arr) + ' ' + Math.max(...s_arr);
}
