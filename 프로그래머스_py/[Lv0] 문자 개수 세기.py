def solution(my_string):
    # in 아스키 코드
    # A = 65, a = 97
    
    answer = [0 for i in range(52)]
    
    for s in my_string:
        # ord(): 문자 -> 아스키 코드
        if ord(s) < ord('a'): # 대문자
            answer[ord(s) - ord('A')] += 1
        else: # 소문자
            answer[ord(s) - ord('a') + 26] += 1
            
    return answer
