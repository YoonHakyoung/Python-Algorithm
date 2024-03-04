def solution(brown, yellow):
    # x + y = brown / 2 + 2
    x_plus_y = int(brown / 2 + 2)
    
    # (x - 2) * (y - 2) = yellow
    # xy = yellow + 2(x + y) - 4
    x_mul_y = int(yellow + 2 * (brown / 2 + 2) - 4)
    
    # 근의 공식
    b = -x_plus_y
    c = x_mul_y
    
    x = (-b + (b**2 - 4*c)**0.5) /2
    y = (-b - (b**2 - 4*c)**0.5) /2

    return [x,y]