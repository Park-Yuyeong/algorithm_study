def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string) // m):
        x = i * m
        answer += my_string[x + (c-1)]
    return answer
