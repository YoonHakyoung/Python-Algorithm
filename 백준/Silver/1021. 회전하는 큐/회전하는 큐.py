N, M = map(int, input().split())
test_list = list(range(1, N+1))
cnt_list = list(map(int, input().split()))
result = 0

for cnt in cnt_list:
    if cnt == test_list[0] : 
        test_list.remove(cnt)
        continue
    if test_list.index(cnt) < len(test_list)/2:
        while (cnt != test_list[0]) :
            test_list.append(test_list[0])
            test_list.pop(0)
            result += 1
    else:
        while (cnt != test_list[0]) :
            test_list.insert(0, test_list[-1])
            test_list.pop(-1)
            result += 1
    test_list.remove(cnt)

print(result)