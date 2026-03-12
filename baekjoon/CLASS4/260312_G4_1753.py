'''
G4 1753 최단경로

문제 설명:
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
모든 간선의 가중치는 10이하의 자연수.

입력:
첫째 줄 - 정점 개수 V, 간선 개수 E. (1 <= V <= 20000, 1 <= E <= 300000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정.
둘째 줄 - 시작 정점 번호 K (1 <= K <= V).
셋째 줄부터 E개의 줄 - 각 간선을 나타내는 세개의 정수. (u, v, w) 형태로 주어짐.
u에서 v로가는 가중치 w인 간선이라는 뜻.
u, v는 서로 다르며 w는 10 이하 자연수.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수 있음.

출력:
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로값을 출력.
시작점 자신은 0으로 출력. 존재하지 않으면 INF 출력.
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

import heapq

V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    edge[a].append((b, w))

visit = [float('inf')] * (V+1)
visit[K] = 0

hq = [(0, K)]

while hq:
    dist, now = heapq.heappop(hq)

    if visit[now] < dist:
        continue

    for i in edge[now]:
        cost = dist + i[1]

        if cost < visit[i[0]]:
            visit[i[0]] = cost
            heapq.heappush(hq, (cost, i[0]))

for i in range(1, V+1):
    if visit[i] == float('inf'):
        output('INF' + '\n')
    else:
        output(str(visit[i]) + '\n')