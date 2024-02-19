T = int(input())
for t in range(T):
    answer1 = 1
    answer2 = 1
    W, E = map(int, input().split())
    for i in range(W):
        #print(E)
        answer1 *= E
        E -= 1
        answer2 *= (i+1)
    print(int(answer1/answer2))