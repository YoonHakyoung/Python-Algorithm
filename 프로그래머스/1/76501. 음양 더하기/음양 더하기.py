def solution(absolutes, signs):
    answer = []
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == True: answer.append(absolutes[i])
        else : answer.append(0-absolutes[i])
    for a in answer:
        result += a
    return result