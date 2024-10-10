def solution(n): 
    x = 0
    while n >= x**2:    #n이 x의 제곱보다 클 때 반복
        x += 1  #x가 1부터 1씩 증가
        if n == x**2:   #만약 x의 제곱이 n과 일치한다면 x+1의 제곱을 출력
            return (x+1)**2
        
    if n != x**2:   #n이 어느 무엇의 제곱도 아닐 경우 -1 반환
        return -1
    
print(solution(int(input())))