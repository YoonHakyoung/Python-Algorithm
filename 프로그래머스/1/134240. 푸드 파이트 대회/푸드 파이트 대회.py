def solution(food):
    answer = []
    cnt_list = []
    
    for f in food:
        cnt_list.append(f//2)

    cnt_list = cnt_list[1:]
    
    for i in range(1, len(cnt_list)+1):
        if cnt_list[i-1] != 0:
            answer.append(str(i)*cnt_list[i-1])
    
    answer.append(0)
    
    for i in range(len(cnt_list)+1, 1, -1):

        if cnt_list[i-2] != 0:
            answer.append(str(i-1)*cnt_list[i-2])
            
    for a in range(len(answer)):
         answer[a] = str(answer[a])

    answer = ''.join(answer)

    return answer 