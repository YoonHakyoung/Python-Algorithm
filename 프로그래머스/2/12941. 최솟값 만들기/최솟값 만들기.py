def solution(A,B):
    sumlist = []
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sumlist.append(A[i]*B[i])
    return sum(sumlist)