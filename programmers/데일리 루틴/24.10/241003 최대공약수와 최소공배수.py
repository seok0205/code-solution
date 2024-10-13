def solution(n, m):
    # 최대 공약수 구하기
    for i in range(min(n, m), 0, -1): #둘 중 작은수부터 0까지 감소하며 반복.
        if (n % i == 0) and (m % i == 0):   #i가 두 수에 모두 나누어 떨어진다면,
            a = i   #반복 중단. '최대' 공약수이기 때문이다.
            break
    # 최소 공배수 구하기        
    for j in range(max(n, m), (n * m) + 1): #둘 중 큰 수부터 두 수의 곱까지. 왜냐면 공배수는 두 수보다 작을 수 없기 때문.
        if j % n == 0 and j % m == 0: #j가 둘다 나누어 떨어진다면
            b = j   #반복 중단. '최소' 공배수라서.
            break
        
    return [a, b]