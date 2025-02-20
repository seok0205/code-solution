'''
D3 16674 미로의 거리

NxN 미로에서 출발지, 목적지 주어짐
최소 몇 개의 칸을 지나면 도착지에 다다를 수 있는지 출력
못가는 경우 0
'''

from collections import deque


def bfs(s, e):
    visited = [[0] * N for _ in range(N)]   # 미로 방문기록 담을 기록표

    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1     # 시작점은 1

    di = [1, 0, -1, 0]      # 델타 활용
    dj = [0, 1, 0, -1]

    while q:
        s = q.popleft()     # 디큐

        for k in range(4):      # 현재 좌표의 4방향 모두 탐색
            x = s[0] + di[k]
            y = s[1] + dj[k]
            if 0 <= x < N and 0 <= y < N and not visited[x][y] and maze[x][y] != '1':       # 좌표가 미로 안이고, 방문한적이 없으며, 벽이 아니라면
                q.append((x, y))        # 가야 할 곳
                visited[x][y] = visited[s[0]][s[1]] + 1     # 방문 기록 순서(방문중인 노드의 값에 +1)

    if visited[e[0]][e[1]] == 0:        # 만약 도착점이 0이면 경로가 없다는 뜻
        return 0

    return visited[e[0]][e[1]] - 2      # 도착점과 출발점의 사이 거리이기 때문에 도착점에서 2를 빼주면 중간 칸 거리임


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    start = tuple()
    end = tuple()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':   # 출발점
                start = (i, j)
            if maze[i][j] == '3':   # 도착점
                end = (i, j)

    result = bfs(start, end)

    print(f'#{tc} {result}')
