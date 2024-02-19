N = int(input())
for i in range(N-1, -1, -1):
    print(' '*i + '*'*(1+2*(N-1-i)))
for j in range(1, N):
    print(' '*j + '*'*(1+2*(N-1-j)))