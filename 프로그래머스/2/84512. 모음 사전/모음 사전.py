def solution(word): # "AAAAE"
    answer = 0
    myList = ['A', 'E', 'I', 'O', 'U']
    plusNum = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += (plusNum[i] * myList.index(word[i]) + 1)
    return answer