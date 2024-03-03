def solution(s):
    answer = []
    
    def change(s):
        countZero = s.count('0')
        countOne = s.count('1')
        changeBin = bin(countOne)[2:]
        return [countZero, changeBin]
    
    countZero = change(s)[0]
    changeBin = change(s)[1]
    changeBinCount = 1
    
    while changeBin != '1':
        result = change(changeBin)
        countZero += result[0]
        changeBin = result[1]
        changeBinCount += 1
    
    answer = [changeBinCount, countZero]
        
    return answer