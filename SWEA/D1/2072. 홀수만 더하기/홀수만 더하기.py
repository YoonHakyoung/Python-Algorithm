T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr_sum = sum(x for x in arr if x % 2 == 1)
    print(f"#{test_case} {arr_sum}")