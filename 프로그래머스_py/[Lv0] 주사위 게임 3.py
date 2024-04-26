def solution(a, b, c, d):
    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0} # 주사위 표현에 dictionary 활용
    answer = 0
    diff = []
    
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    dice[d] += 1
    
    # set() 함수 활용 - 나온 숫자 종류의 개수 확인
    if len(set([a, b, c, d])) == 1: # 4 숫자가 모두 p로 같은 경우
        return 1111 * a
    elif len(set([a, b, c, d])) == 4: # 4 숫자가 모두 다른 경우
        return min([a, b, c, d])
    elif len(set([a, b, c, d])) == 3: # 4 숫자 중 2 숫자가 같고 나머지 숫자들은 다른 경우
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
            
    max_value = max(dice.values())
            
    if max_value == 3: # 4 숫자 중 3 숫자가 같은 경우
        return answer**2
    
    # 4 숫자가 두 개씩 값이 같은 경우
    return answer * abs(diff[0] - diff[1])
