'''
D3 16532 미로

NxN 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인
도착 가능 시 1, 아니면 0
'''


def find_maze(matrix, s):
    visited = matrix.copy()
    stack = list()
    stack.append(s)

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while True:
        if visited[s[0]][s[1]] == '3':      # 목적인 '3'을 만나면 1반환
            return 1
        if visited[s[0]][s[1]] == '0' or visited[s[0]][s[1]] == '2':    # '3'을 발견하기 전까지 방문할 곳은 '0'이나 '2'밖에 없어서
            visited[s[0]][s[1]] = 1     # 방문한 흔적 남김
        for k in range(4):
            x = s[0] + di[k]
            y = s[1] + dj[k]
            if 0 <= x < N and 0 <= y < N and visited[x][y] != '1':      # 델타를 활용해 4방향 모두를 봤을때, 미로안의 좌표이고 '1'(벽)이 아니면
                if visited[x][y] == '0' or visited[x][y] == '3':        # 거기에 '0'이나 '3'이면 그곳으로 이동할 예정
                    stack.append([s[0], s[1]])                          # 현재 좌표 stack에 추가하고
                    s = [x, y]                                          # 다음 좌표 설정
                    break
        else:
            if stack:       # 스택에 돌아갈 곳 있으면 팝해서 돌아감
                s = stack.pop()
            else:           # 목표 찾지 못하고 돌아갈 곳 없으면 while문 중단
                break
    return 0        # 목표 못찾았으므로 0 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(str, input())) for _ in range(N)]

    for i in range(N):      # 시작점 '2'를 찾는 코드
        for j in range(N):
            if maze[i][j] == '2':
                start = [i, j]
                break

    print(f'#{tc} {find_maze(maze, start)}')
