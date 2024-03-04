def solution(n):
    answer = 0
    for m in range(n//2):
        i = m + 1
        addResult = 0
        while addResult <= n:
            addResult += i
            if addResult == n: 
                answer += 1
            i += 1
    return answer + 1