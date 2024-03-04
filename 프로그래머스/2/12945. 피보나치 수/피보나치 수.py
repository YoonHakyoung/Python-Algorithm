def solution(n):
    answer = 0
    pivoList = [0, 1]
    for i in range(2, n + 1):
        pivoList.append(pivoList[i-1]+pivoList[i-2])

    answer = pivoList[-1] % 1234567

    return answer