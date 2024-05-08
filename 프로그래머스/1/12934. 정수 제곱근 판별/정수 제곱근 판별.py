def solution(n):
    if ((n**(1/2)) - int(n**(1/2))) == 0.0:
        return ((int(n**(1/2)) + 1) ** 2)
    else: return -1
