def solution(a, b): #내적을 구할 두 행렬을 입력받는다.
    result = 0
    for i in range(len(a)): #행렬 내적은 a[0]*b[0] + a[1]*b[1] +... +a[n]*b[n]이다.
        result += a[i]*b[i]
    return result