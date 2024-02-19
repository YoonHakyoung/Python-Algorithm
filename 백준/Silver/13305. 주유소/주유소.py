N = int(input()) # 4
Len = list(map(int, input().split())) # 2 3 1
Prc = list(map(int, input().split())) # 5 2 4 1
answer = Prc[0] * Len[0] # 출발할 때 

for i in range(1, N-1):
    if Prc[i] == min(Prc): # 최저가 
        answer += Prc[i] * sum(Len[i:])
        break
    if Prc[i] < Prc[i-1]:
        answer += Prc[i] * Len[i] # 전 마을보다 가격 더 싸면 
    else:
        answer += Prc[i-1] * Len[i]

print(answer)