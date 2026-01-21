'''
S2 1260 DFS와 BFS

그래프를 DFS, BFS로 탐색한 결과를 출력하는 프로그램 작성.
방문 가능한 점이 여러개면 정점번호가 작은것부터 방문, 더이상 없으면 종료.
정점 번호는 1부터 N까지.

입력:
첫째 줄 - 정점 개수 N (1~1000), 간선 개수 (1~10,000), 탐색 시작 정점 번호 V.
다음 M개의 줄에는 연결된 정점 번호. 두 정점 사이에 여러 개의 간선있을 수 있음. 양방향.

출력:
첫 줄은 DFS 수행 결과, 다음 줄엔 BFS 결과 출력.
V부터 방문된 점을 순서대로 출력.
'''

import sys
# sys.stdin = open('tc.txt')
input = sys.stdin.readline
pp = sys.stdout.write


def dfs(N, V, edge):
    result = []
    stack = [V]
    cnt = [0] * (N+1)
    cnt[V] = 1
    result.append(V)

    while stack:
        x = stack[-1]
        found = False

        for i in sorted(edge[x]):
            if not cnt[i]:
                cnt[i] = 1
                result.append(i)
                stack.append(i)
                found = True
                break
        if not found:
            stack.pop()
    
    pp(' '.join(map(str, result)) + '\n')


def bfs(N, V, edge):
    result = []
    q = [V]
    cnt = [0] * (N+1)
    cnt[V] = 1

    while q:
        x = q.pop(0)
        result.append(x)
        for i in sorted(edge[x]):
            if not cnt[i]:
                cnt[i] = 1
                q.append(i)

    pp(' '.join(map(str, result)) + '\n')


def solution():
    N, M, V = map(int, input().split())
    edge = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    dfs(N, V, edge)
    bfs(N, V, edge)


solution()