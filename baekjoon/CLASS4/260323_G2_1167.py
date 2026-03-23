'''
G2 1167 트리의 지름

문제 설명:
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램 작성.

입력:
트리가 입력으로 주어짐.
첫 줄 - V (2 <= V <= 100,000)
둘째 줄부터 V개 줄에 걸쳐 간선 정보가 주어짐.
1부터 V까지 매겨져있음.
(정점번호, 이어진 정점번호, 그 정점까지의 거리, -1), 이어진 정점번호와 거리는 여러개일 수 있음.
'''

import sys
# sys.stdin = open('tc.txt')
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque

V = int(input())
edge = [[] for _ in range(V+1)]

for _ in range(1, V+1):
    data = list(map(int, input().split()))
    if len(data) == 2:
        continue

    for i in range(1, len(data)-1, 2):
        edge[data[0]].append((data[i], data[i+1]))


def bfs(s):
    visit = [-1] * (V+1)
    q = deque([s])
    visit[s] = 0
    max_dist = 0
    far_node = s

    while q:
        now = q.popleft()

        for node, dist in edge[now]:
            if visit[node] == -1:
                visit[node] = visit[now] + dist
                q.append(node)
                if visit[node] > max_dist:
                    max_dist = visit[node]
                    far_node = node
    
    return far_node, max_dist


a, b = bfs(1)
c, d = bfs(a)
output(str(d))