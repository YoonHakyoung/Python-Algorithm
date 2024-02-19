def solution(s):
    s = list(s)
    n_list = ['('] # 괄호 완성 여부 확인용 리스트
    
    if s[0] == ')' or s[-1] == '(' : return False
    
    for i in range(1, len(s)):
        
        # 괄호 완성이면 리스트에서 제거
        if n_list != [] and n_list[-1] == '(' and s[i] == ')':
            n_list.pop(-1)
            
        # 괄호 미완성이면 리스트에 추가
        else : 
            n_list.append(s[i])
            
    if n_list == [] : return True
    else : return False