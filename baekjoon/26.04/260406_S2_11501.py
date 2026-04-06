'''
S2 11501 주식

문제 설명:
요즘 주식에 빠져 있음.
날 별로 주가를 예상 가능하고 그게 언제나 맞음.

1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

날 별로 주식의 가격을 알 때, 최대 이익이 얼마나 되는지 계산하려고 함.

날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익이 0임.
만약 날 별로 주가가 3, 5, 9면 처음 두날에 주식을 하나씩 사고, 마지막날 다팔면 이익이 10임.

입력:
첫 줄 - T
테스트케이스 별 첫 줄 - 날의 수 자연수 N(2 <= N <= 1,000,000)
둘째 줄 - 날 별 주가를 나타내는 N개의 자연수(각 수는 10,000 이하)가 순서대로 주어짐. 공백으로 구분.

출력:
각 TC별로 최대 이익을 나타내는 정수 하나 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    costs = list(map(int, input().split()))
    max_idx = N-1

    max_price = 0
    earn = 0
    
    for i in range(N-1, -1, -1):
        if costs[i] > max_price:
            max_price = costs[i]
        else:
            earn += (max_price - costs[i])

    print(earn)