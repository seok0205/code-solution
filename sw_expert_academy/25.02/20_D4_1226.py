'''
D4 1226 미로 1

16x16 행렬의 형태 미로에서 시작점, 도착점이 주어짐
갈 수 있는지 판단하는 문제
가능하면 1 불가능하면 0
'''

from collections import deque


def find_end(matrix):       # 끝 좌표 찾기
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == '3':     # '3'이 도착점.
                return i, j


def find_way(s, e):         # BFS 활용
    di = [0, 0, 1, -1]      # 델타
    dj = [1, -1, 0, 0]

    visited = [[0] * 16 for _ in range(16)]     # 방문 기록
    q = deque()
    q.append(s)     # 첫 값 인큐
    visited[s[0]][s[1]] = 1     # 방문 기록 남기기

    while q:        # 큐에 값이 있으면 계속 실행
        s = q.popleft()     # 디큐
        if visited[s[0]][s[1]] == 0:
            visited[s[0]][s[1]] = 1
        for k in range(4):      # 4방향 모두 탐색
            x = s[0] + di[k]
            y = s[1] + dj[k]
            if 0 <= x < 16 and 0 <= y < 16 and not visited[x][y] and maze[x][y] != '1':     # 만약 미로내이고 방문한적없고, 벽이아니면.
                q.append((x, y))    # 다음 방문할 노드 인큐

    if visited[e[0]][e[1]]:     # 만약 도착점에 방문을 했으면 루트가 존재
        return 1
    else:                       # 만약 도착점의 값이 0이면 경로 없다는 뜻
        return 0


T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    maze = [list(input()) for _ in range(16)]

    start = (1, 1)
    end = find_end(maze)
    result = find_way(start, end)

    print(f'#{tc_num} {result}')