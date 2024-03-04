def solution(s):
    sList = list(str(s))
    answer = [s[0]]
    for s in range(1, len(sList)):
        if answer != [] and answer[-1] == sList[s]:
            del answer[-1]
        else:
            answer.append(sList[s])
    if answer == []: return 1
    return 0