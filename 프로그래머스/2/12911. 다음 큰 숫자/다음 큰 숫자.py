def solution(n):
    answer = 0
    inputNum = bin(n)[2:]
    inputNumOne = str(inputNum).count('1')
    
    nextNum = 0
    nextNumOne = 0
    i = 1
    while inputNumOne != nextNumOne:
        nextNum = bin(n + i)[2:]
        nextNumOne = str(nextNum).count('1')
        answer = n + i
        i += 1
        
    return answer