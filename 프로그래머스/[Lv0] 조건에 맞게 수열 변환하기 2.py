def arrCheck(arr): # 조건에 맞게 수열 변환하기 1 코드 재사용
    for i in range(len(arr)):
        if arr[i] >= 50 and not(arr[i] % 2):
            arr[i] //= 2
        elif arr[i] < 50 and arr[i] % 2:
            arr[i] = arr[i] * 2 + 1
    return arr

def solution(arr):
    answer = 0
    a = arr.copy() # a = arr을 하면 arr와 a가 같은 주소 공간을 참조 
    check = arrCheck(arr)
    while a != check:
        a, arr, check = check.copy(), check, arrCheck(arr)
        answer += 1
    return answer
