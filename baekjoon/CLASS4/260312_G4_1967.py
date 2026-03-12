'''
G4 1967 트리의 지름

문제 설명:
트리의 지름은 트리에 존재하는 모든 경로들 중 가장 긴것의 길이를 말함.
입력으로 루트가 있는 길이는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램 작성.
트리의 노드는 1부터 n까지 번호가 매겨져있음.

입력:
첫 줄 - 노드 개수 n (1 <= n <= 10,000)
둘째 줄부터 n-1개의 줄 - 간선 정보(부모노드 번호, 자식노드 번호, 가중치)
간선 정보는 부모 노드 번호가 작은 것부터 입력.
부모 노드가 같으면 자식 노드의 번호가 작은 게 먼저 입력. 루트 노드 번호는 항상 1이라 가정.
가중치는 100보다 크지 않은 양의 정수가 입력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))


def bfs(node, status):
    visit = [0] * (n+1)
    dist = [0] * (n+1)
    visit[node] = 1
    q = deque([node])

    while q:
        x = q.popleft()

        for i in tree[x]:
            if visit[i[0]]:
                continue
            
            visit[i[0]] = 1
            dist[i[0]] = dist[x] + i[1]
            q.append(i[0])
    
    if not status:
        answer = dist.index(max(dist))
    else:
        answer = max(dist)
    return answer

node = bfs(1, 0)
result = bfs(node, 1)
output(str(result))