def solution(todo_list, finished):
    answer = []
    for i, l in enumerate(todo_list):
        if not(finished[i]):
            answer.append(l)
    return answer
