T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    NN = []
    # 파리 개수 배열 넣기
    for n in range(N):
        NN.append(list(map(int, input().split())))

    result = 0
    # 파리채 모양으로 5, 3이면 3번
    for i in range(N-M+1):
        for j in range(N-M+1):
            m_sum = sum(sum(row[j:j+M]) for row in NN[i:i+M])
            if result > m_sum:
                pass
            else:
                result = m_sum

    print("#{0} {1}".format(t+1,result))