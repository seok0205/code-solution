'''
양의 정수 n이 주어짐. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수가 몇 개인지 알아보려 함.

소수 양쪽에 0이 있는 경우 ex. 0P0
소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우 ex. P0
소수 왼쪽에만 0이 있고 오른쪽에 아무것도 없는 경우 ex. 0P
소수 양쪽에 아무것도 없는 경우 ex. P
단, P는 각 자릿수에 0을 포함하지 않는 소수.
ex. 101은 P가 될 수 없다.

제한 사항 :
1 <= n <= 1,000,000
3 <= k <= 10

접근 :
1. 주어진 수를 k진법화 한다.
2. 0으로 수를 split하고, 차례로 cnt 변수로 소수 개수를 구함.
'''

n = 437674
k = 3

def k_num(n,k): 
    '''k진법화하여 num 출력.'''
    num = ''
    while n > 0:    # num을 k진법화하는 방법.
        num += str(n % k)
        n //= k
    return num[::-1]    # 거꾸로 뒤집기

def sosu(n):
    '''소수인지 판별하는 함수'''
    if n < 2:   # 1이면 아님.
        return False
    for i in range(2, int(n ** 0.5) + 1):   # 2부터 i를 반으로 나눈 지점까지,(나머지 반은 똑같은 형태를 보이기 때문.)
        if n % i == 0:  # 나누어 떨어지면 소수가 아님.
            return False
    return True # 위조건 만족시 소수.

def solution(n, k):
    result = 0
    num = k_num(n,k)    # k진법화
    for i in num.split("0"):    # 0으로 split.
        if len(i) > 0:  # i의 자릿수가 0보다 클때,
            if sosu(int(i)):    # 소수판별조건 만족 시
                result += 1 # 개수 증가
    return result

print(solution(n,k))