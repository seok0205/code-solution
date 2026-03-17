'''
G4 14938 서강그라운드

문제 설명:
각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다.
예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.

입력:
첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.

둘째 줄에는 n개의 숫자가 차례대로 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.
세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.
지역의 번호는 1이상 n이하의 정수이다.
두 지역의 번호가 같은 경우는 없다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
visit = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    visit[i][i] = 0

for _ in range(r):
    a, b, dist = map(int, input().split())
    visit[a][b] = min(visit[a][b], dist)
    visit[b][a] = min(visit[b][a], dist)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visit[i][j] > visit[i][k] + visit[k][j]:
                visit[i][j] = visit[i][k] + visit[k][j]

max_item = 0

for i in range(1, n+1):
    now = 0
    for j in range(1, n+1):
        if visit[i][j] <= m:
            now += items[j]
    
    max_item = max(max_item, now)

output(str(max_item))

# 위 풀이는 플로이드 워셜, 아래는 다익스트라

import heapq

def dijkstra(start, n, adj):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    
    hq = [(0, start)]
    
    while hq:
        cost, now = heapq.heappop(hq)
        
        if dist[now] < cost:
            continue
            
        for v, w in adj[now]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(hq, (new_cost, v))
                
    return dist

def solve():
    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))
    
    roads = [[] for _ in range(n + 1)]
    for _ in range(r):
        u, v, w = map(int, input().split())
        roads[u].append((v, w))
        roads[v].append((u, w))
    
    max_items = 0
    
    for i in range(1, n + 1):
        distances = dijkstra(i, n, roads)
        
        now = 0
        for j in range(1, n + 1):
            if distances[j] <= m:
                now += items[j]
        
        max_items = max(max_items, now)
        
    output(str(max_items))