'''
G5 15989 1, 2, 3 더하기 4

문제 설명:
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지.
합을 나타낼 때는 수를 1개 이상 사용해야 함.
합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

- 1+1+1+1
- 2+1+1 (1+2+1, 1+1+2)
- 2+2
- 1+3 (3+1)

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제.

입력:
첫째 줄 - TC 개수 T
TC는 한줄(정수 n) - n은 양수이고 10,000보다 작거나 같음.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

dp = [0] * 10001
dp[0] = 1

for i in range(1, 10001):
    dp[i] += dp[i-1]

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]    

T = int(input())

for _ in range(T):
    n = int(input())

    print(dp[n])
    
    

    