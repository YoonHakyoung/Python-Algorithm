def solution(arr):
    answer = 0
    arr.sort(reverse=True) # 배열 정렬
    
    # answer을 arr 마지막 값의 배수로 순차적 진행
    answer = arr[0]
    while (True):
        for i in arr[1:]:
            if answer % i != 0 : 
                break
            elif i == arr[-1] : 
                return answer
        answer += arr[0]
    return answer