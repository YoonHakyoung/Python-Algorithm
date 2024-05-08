def solution(a, b):
    answer = 0
    if a == b : return a
    # 3 7
    elif abs(a-b) % 2 == 0: 
        if a < b :
            answer += (b - ( abs(a-b) / 2 ))
            answer += (a + b) * ( abs(a-b) / 2 )
            return answer
        else :
            answer += (a - ( abs(a-b) / 2 ))
            answer += (a + b) * ( abs(a-b) / 2 )
            return answer
    # 3 6
    else :
        answer += (a + b) * ( abs(a-b) // 2 + 1 )
        return answer