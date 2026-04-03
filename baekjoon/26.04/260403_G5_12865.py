'''
G5 12865 평범한 배낭(재풀이)

문제 설명:
여행을 가려고함.
여행에 필요하다고 생각되는 N개의 물건이 있음.
각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배당에 넣어서 가면 V만큼 즐길 수 있음.

최대 K만큼의 무게만을 넣을 수 있는 배낭을 들고 다님.
최대한 즐겁게 여행하기 위해 배낭에 넣을 수 있는 물건들의 최댓값을 구하는 문제.

입력:
첫 줄 - 물품의 수 N(1 <= N <= 100), 버틸 수 있는 무게 K (1 <= K <= 100,000)
두번째 줄부터 N개의 줄 - 물건 무게 W(1 <= W <= 100,000), 물건 가치 V(1 <= V <= 1,000)이 주어짐.
입력은 모두 정수.

출력:
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K+1)
items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

for w, v in items:
    for i in range(K, w - 1, -1):
        if dp[i] < dp[i-w] + v:
            dp[i] = dp[i-w] + v

print(dp[K])