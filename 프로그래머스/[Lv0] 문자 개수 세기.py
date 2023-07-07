def solution(my_string):
    # in 아스키 코드
    # A = 65, a = 97
    
    answer = [0 for i in range(52)]
    
    for s in my_string:
        # ord(): 문자 -> 아스키 코드
        if ord(s) < 97: # 대문자
            answer[ord(s) - 65] += 1
        else: # 소문자
            answer[ord(s) - 71] += 1
            
    return answer
