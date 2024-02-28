def solution(clothes):
    answer = 1
    mydict = {}
    for i in clothes:
        mydict[i[1]] = 0
    
    for i in clothes:
        mydict[i[1]] += 1
    
    for i in mydict.values():
        answer *= (i + 1)
        
    return answer - 1