def solution(a, b):
    aplusb = int(str(a) + str(b))
    bplusa = int(str(b) + str(a))
    
    if aplusb >= bplusa:
        return aplusb
    else:
        return bplusa
