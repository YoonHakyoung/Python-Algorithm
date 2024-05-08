def solution(x):
    result = 0
    x_list = list(str(x))
    for i in range(len(x_list)):
        result += int(x_list[i])
    if x % result == 0: return True
    else : return False