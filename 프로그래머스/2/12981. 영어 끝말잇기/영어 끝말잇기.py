def solution(n, words):
    answer = []
    for i in range(1, len(words)):
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            num = i % n + 1
            order = i // n + 1
            answer = [num, order]
            break
    if answer == [] : return [0, 0]
    return answer