def solution(code):
    mode = 0
    ret = ''
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode ^= 1 # 비트 연산자를 활용한 mode 변환
            continue
        
        if idx % 2 == mode:
            ret += code[idx]
    
    return ret if ret != '' else 'EMPTY'
