'''
G3 11779 최소비용 구하기 2

문제 설명:
n(1 <= n <= 1000)개의 도시가 있음.
한 도시에서 출발하여 다른 도시에 도착하는 m(1 <= m <= 100,000)개의 버스가 있음.
A번째 도시에서 B번째 도시까지 가는 데 드는 비용을 최소화 시키려고 함.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용과 경로를 출력.
항상 시작점에서 도착점으로의 경로가 존재함.

입력:
첫째 줄 - n
둘째 줄 - m
셋째 줄부터 m줄에 버스의 정보.
(출발 도시 번호, 도착 도시 번호, 버스 비용)
버스 비용은 0보다 크거나 같고 100,000보다 작은 정수
마지막줄에는 구하고자 하는 출발, 도착 도시 번호.

출력:
첫째 줄 - 출발 도시에서 도착도시까지 가는 데 드는 최소 비용.
둘째 줄 - 최소 비용을 갖는 경로에 포함되는 도시 개수 출력. 출발 및 도착 도시도 포함.
셋째 줄 - 경로 방문 도시 순서대로 출력. 경로가 여러가지면 아무거나 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

import heapq

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))

start, end = map(int, input().split())
visit = [float('inf')] * (n+1)
visit[start] = 0
parents = [0] * (n+1)
hq = [(0, start)]

while hq:
    cost, now = heapq.heappop(hq)

    if visit[now] < cost:
        continue

    for node, dist in bus[now]:
        new_cost = cost + dist
        if new_cost < visit[node]:
            visit[node] = new_cost
            parents[node] = now
            heapq.heappush(hq, (new_cost, node))

result = []
now = end
while now != 0:
    result.append(now)
    now = parents[now]

result.reverse()

output(str(visit[end]) + '\n')
output(str(len(result)) + '\n')
output(' '.join(map(str, result)))