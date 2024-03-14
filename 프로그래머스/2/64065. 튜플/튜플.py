def solution(s):
    answer = []
    my_dict = {}

    s = s[2:-2]
    s = s.split('},{')
    
    s_list = []
    for i in s:
        iList = list(map(int, i.split(',')))
        s_list.append(iList)
        
    s_list = sorted(s_list, key=len)    # [[3], [2, 3], [4, 2, 3], [2, 3, 4, 1]]
    s_list_1 = sum(s_list, [])          # [3, 2, 3, 4, 2, 3, 2, 3, 4, 1]

    for i in s_list[-1]:    # [2, 3, 4, 1]
        my_dict[i] = s_list_1.count(i)
    
    answer = sorted(my_dict, key=my_dict.get, reverse = True)
    
    return answer
