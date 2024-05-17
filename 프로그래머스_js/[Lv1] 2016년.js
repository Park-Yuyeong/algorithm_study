function solution(a, b) {
    const months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const daysOfTheWeek = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    let days = b;
    
    for(let i = 0; i < a; i++) {
        days += months[i];
    }
    
    return daysOfTheWeek[days % 7];
}
