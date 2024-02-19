def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    
    i = 0
    answer = 0
    
    for i in range(t_len - p_len +1):
        if int(t[i:i+p_len]) <= int(p) :
            answer += 1
        i += 1
    return answer