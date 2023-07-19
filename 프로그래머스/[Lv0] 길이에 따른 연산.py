def multiply(n_list):
    mul = 1
    for n in n_list:
        mul *= n
    return mul

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else multiply(num_list)
