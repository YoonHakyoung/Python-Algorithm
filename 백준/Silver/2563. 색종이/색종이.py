N = int(input())

W = [[0] * 100 for _ in range(100)]

for n in range(N):
    X, Y = map(int, input().split())
    for x in range(X,X+10):
        W[x][Y:Y+10] = [1] * 10

print(sum(sum(W, [])))