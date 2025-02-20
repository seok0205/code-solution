'''
D3 16673 노드의 거리

V개의 노드 개수와 방향성 없는 E개 간선정보 주어짐
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 문제
노드 번호는 1번부터, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있음
'''

from collections import deque


def bfs(s, g):      # BFS 함수
    q = deque()
    visited = [0] * (V+1)
    q.append(s)     # 첫 인큐
    visited[s] = 1  # 방문 기록

    while q:    # 큐에 값이 있다면 계속 반복
        s = q.popleft()     # 디큐
        for w in edge[s]:
            if visited[w] == 0:     # 간선통해 방문 가능한 노드 방문안했다면
                q.append(w)         # 인큐
                visited[w] = visited[s] + 1     # 방문 기록 바로 전 노드의 값에 +1(순서 알수 있음)

    if visited[g] == 0:     # 만약 목표에 방문 안했다면 못가는것
        return 0
    else:       # 값이 있다면
        return visited[g] - 1   # 거리를 구하는 것이므로 마지막 노드의 숫자에서 -1하면 됨


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())

        edge[a].append(b)   # 무방향 그래프라서 왔다갔다가 가능 따라서 두 루트 모두 추가
        edge[b].append(a)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')

