def solution(s):
    temp = list(str(s))
    p_cnt = 0
    y_cnt = 0
    for i in temp:
        if i in ['P', 'p']: p_cnt+=1
        elif i in ['Y', 'y']: y_cnt+=1
        else: pass
    if p_cnt == y_cnt: return True
    else: return False