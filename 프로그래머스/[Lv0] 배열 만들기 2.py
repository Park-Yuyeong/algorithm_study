def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i % 5:
            continue
            
        check = set(str(i))
        isTrue = True
        if len(check) > 2:
            continue
            
        for c in check:
            if c == "0" or c == "5":
                pass
            else:
                isTrue = False
                break
                
        if isTrue:
            answer.append(i)
                     
    return answer if len(answer) else [-1]
