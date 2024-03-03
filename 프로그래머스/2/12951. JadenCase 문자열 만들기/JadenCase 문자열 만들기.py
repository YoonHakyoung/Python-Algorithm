def solution(s):
    answer = ''
    s_list = list(s)
    answer = []
    
    for i in range(len(s_list)):
        if i == 0 or s_list[i-1] == ' ': 
            answer.append(s_list[i].upper())  
        else:
            answer.append(s_list[i].lower())
    answer = ''.join(answer)
    return answer
    