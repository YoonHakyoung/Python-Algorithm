T = int(input()) # 테스트케이스 개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    arr = list(map(int, input().split()))
    if arr[0] == arr[1]: 
    	print(f"#{test_case} =")
    elif arr[0] < arr[1]: 
    	print(f"#{test_case} <")
    else:
        print(f"#{test_case} >")
    # ///////////////////////////////////////////////////////////////////////////////////
