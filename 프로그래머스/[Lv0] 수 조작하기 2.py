def solution(numLog):
    control_dict = {1: "w", -1: "s",  10: "d", -10: "a"}
    
    msg = ''
    for i in range(1, len(numLog)):
        msg += control_dict[numLog[i] - numLog[i-1]]
        
    return msg
