def solution(arr):
    answer = []
    tmp = []
    for n in arr:
        if n == 2:
            answer += tmp + [n]
            tmp = []
        elif answer:
            tmp += [n]
            
    return answer if answer else [-1]
