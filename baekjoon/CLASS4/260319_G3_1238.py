'''
G3 1238 파티

문제 설명:
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있음.
어느날 이 N명의 학생이 X(1 <= X <= N)번 마을에 모여서 파티를 벌이기로 함.
이 마을 사이에는 M개의 단방향 도로들이 있고, i번째 길을 지나는데 T(1 <= T <= 100)의 시간을 소비함.
학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 함.
최단시간에 오고 가기를 원함.
단방향이라 오고 가는 방향이 다를 수 있음. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구인지 구하는 문제.

입력:
첫째 줄 - N, M, X가 공백으로 구분되어 입력.
두번째 줄부터 M개의 줄동안 i번째 도로의 시작점, 끝점, T가 주어짐.
시작점 끝점 같은 도로는 없고, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개.
모든 학생들은 집에서 X로 갈수 있고, X에서 집으로 올수 있는 데이터만 입력으로 주어짐.

출력:
N명의 핛애들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

import heapq

N, M, X = map(int, input().split())
edge = [[] for _ in range(N+1)]
reverse = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    edge[a].append((b, t))
    reverse[b].append((a, t))

def func(s, g):
    visit = [float('inf')] * (N+1)
    visit[s] = 0
    hq = [(0, s)]

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > visit[now]:
            continue

        for node, cost in g[now]:
            new_cost = dist + cost
            if new_cost < visit[node]:
                visit[node] = new_cost
                heapq.heappush(hq, (new_cost, node))

    return visit

go = func(X, reverse)
back = func(X, edge)
result = 0

for i in range(1, N+1):
    total = go[i] + back[i]
    if total > result:
        result = total

output(str(result))