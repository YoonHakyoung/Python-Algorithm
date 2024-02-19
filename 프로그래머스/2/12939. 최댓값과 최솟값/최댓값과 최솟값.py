def solution(s):
    input_list = s.split()
    resul_list = []
    for i in input_list:
        resul_list.append(int(i))
    
    answer = []
    answer.append(str(min(resul_list)))
    answer.append(' ')
    answer.append(str(max(resul_list)))

    answer = ''.join(answer)
    
    return answer