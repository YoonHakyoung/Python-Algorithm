def solution(s):
    answer = []
    i = 0
    for i in range(len(s)): # 리스트 길이만큼
        if s[i] in s[0:i]: # 앞에 같은 문자가 있다면
            for j in range(len(s[0:i])): # 자른 리스트 길이 만큼
                if s[i] == s[j]: 
                    position = len(s[0:i]) - j              
            answer.append(position)
        else: answer.append(-1)
    return answer