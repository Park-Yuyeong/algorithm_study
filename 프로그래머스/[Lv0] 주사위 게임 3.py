def solution(a, b, c, d):
    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    answer = 0
    diff = []
    
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    dice[d] += 1
    
    max_value = max(dice.values())
    
    if len(set([a, b, c, d])) == 1:
        return 1111 * a
    elif len(set([a, b, c, d])) == 4:
        return min([a, b, c, d])
    elif len(set([a, b, c, d])) == 3:
        answer = 1
        for k, v in dice.items():
            if v == 1:
                answer *= k
        return answer

    for k, v in dice.items():
        if v == 1:
            answer += k
        elif v == 3:
            answer += 10 * k
        elif v == 2:
            answer += k
            diff.append(k)
            
    if max_value == 3:
        return answer**2
    
    return answer * abs(diff[0] - diff[1])
