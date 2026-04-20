'''
G5 5972 택배 배송

문제 설명:
농부 1이 농부 2에게 택배를 배달해야 함.
가는 길에 모든 소들에게 여물을 줘야함.
농부1은 구두쇠라서 최소한의 소를 만나려고 함.

N (1 <= N <= 50,000)개의 헛간
M (1 <= M <= 50,000)개의 길
각 길에 C_i (0 <= C_i <= 1,000)마리의 소가 있음.
소들의 길은 두 개의 떨어진 헛간인 A_i, B_i를 이음.
(1 <= A_i <= N, 1 <= B_i <= N, A_i != B_i)

두 개의 헛간은 하나 이상의 길로 연결되있을 수 있음.
농부 1은 헛간 1에 있고, 농부 2는 헛간 N에 있음.

농부 1의 지도랑 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때, 최소 여물은 얼마인지 구하는 문제.
가는 길의 길이는 고려하지 않음.

입력:
첫째 줄 - N, M이 공백두고 주어짐.
둘째 줄부터 M+1번째 줄까지 A_i, B_i, C_i가 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())
connection = [[] for _ in range(N+1)]
visit = [float('inf')] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    connection[a].append((b, c))
    connection[b].append((a, c))

visit[1] = 0
hq = [(0, 1)]

while hq:
    now_cost, now = heapq.heappop(hq)
    
    if visit[now] < now_cost:
        continue

    for next_loc, cost in connection[now]:
        new_cost = now_cost + cost

        if visit[next_loc] > new_cost:
            heapq.heappush(hq, (new_cost, next_loc))
            visit[next_loc] = new_cost

print(visit[N])