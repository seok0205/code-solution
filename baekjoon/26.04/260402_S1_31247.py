'''
S1 31247 2024는 무엇이 특별할까?

문제 설명:
to(n)을 n의 약수이면서 홀수인 양의 정수의 개수.
te(n)을 n의 약수이면서 짝수인 양의 정수의 개수.
te(2024) = 3to(2024)를 만족함.

이러한 다음 숫자는 2040.

te(x) = K * to(x)를 만족하는 양의 정수 x를 K - 특별한수 로 정의한다.
양의 정수 N과 음이 아닌 정수 K가 주어짐.
N이하의 양의 정수 중 K-특별한 수의 개수를 출력.

입력:
T - 테스트 케이스 개수
TC는 한줄로 구성. 각각 N과 음이 아닌 정수 K가 공백 두고 주어짐.
(1 <= T <= 100,000, 1 <= N <= 10**18, 0 <= K <= 10**18)

출력:
한줄에 하나씩 N 이하의 양의 정수중 K -특별한수의 개수를 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    if K >= 60:
        print(0)
        continue

    m = N // (2**K)

    result = (m+1) // 2
    print(result)