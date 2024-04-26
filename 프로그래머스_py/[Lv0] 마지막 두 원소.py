def solution(num_list):
    n = num_list[-1]
    m = num_list[-2]
    return num_list + [n - m] if n > m else num_list + [n * 2]
