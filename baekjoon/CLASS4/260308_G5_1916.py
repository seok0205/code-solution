'''
1916 G5 최소비용 구하기

문제 설명:
N개의 도시가 있음. 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있음. A번째 도시에서 B번째 도시까지 가는 데 드는 비용을 최소화하려고 함.
A번째 도시에서 B번째 도시로 가는 데 드는 최소 비용을 출력.
도시 번호는 1부터 N.

입력:
첫째 줄 - N (1 <= N <= 1,000)
둘째 줄 - M (1 <= M <= 100,000)
셋째 줄부터 M+2 줄까지 버스 정보. (출발 도시 번호, 도착지 도시 번호, 비용)
버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수
M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어짐. 출발점에서 도착점을 갈 수 있는 경우만 주어짐.
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

import heapq

N = int(input())
M = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    edge[s].append((e, cost))

a, b = map(int, input().split())
visit = [float('inf')] * (N+1)
hq = []

heapq.heappush(hq, (0, a))
visit[a] = 0

while hq:
    cost, now = heapq.heappop(hq)

    if visit[now] < cost:
        continue

    for i in edge[now]:
        new_cost = cost + i[1]

        if new_cost < visit[i[0]]:
            visit[i[0]] = new_cost
            heapq.heappush(hq, (new_cost, i[0]))

output(str(visit[b]))