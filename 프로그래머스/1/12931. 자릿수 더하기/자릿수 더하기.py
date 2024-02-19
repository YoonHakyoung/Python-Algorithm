def solution(n):
    answer = 0
    num_ran=len(str(n))-1
    for i in range(num_ran,-1,-1):
        answer += n//10**i
        n -= (n//10**i) * (10**i)
    
    return answer