function solution(cards1, cards2, goal) {
    let card1 = cards1.shift();
    let card2 = cards2.shift();
    
    for (let word of goal){        
        if (card1 === word){
            card1 = cards1.shift();
        } else if (card2 === word) {
            card2 = cards2.shift();
        } else {
            return 'No';
        }
    }
    
    return 'Yes';
}
