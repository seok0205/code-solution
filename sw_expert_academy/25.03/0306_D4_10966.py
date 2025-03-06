'''
D4 10966 물놀이를 가자

NxM 격자로 표현 가능. 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이 되면 W, 땅이면 L로 표현
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복해 다른 칸으로 이동 가능
격자 밖으로 나가는 이동은 불가능
땅으로 표현된 모든 칸에 대해서 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수 구하고, 모든 이동 횟수의 합 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')


from collections import deque


def bfs(s):
    visit = [[0] * M for _ in range(N)]
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    q = deque()
    q.append(s)
    visit[s[0]][s[1]] = 1

    while q:
        location = q.popleft()
        for k in range(4):
            x = location[0] + di[k]
            y = location[1] + dj[k]
            if 0 <= x < N and 0 <= y < M and visit[x][y] == 0:
                if field[x][y] == 'L':
                    q.append((x, y))
                    visit[x][y] = visit[location[0]][location[1]] + 1
                else:
                    return visit[location[0]][location[1]]
    
    num_sum = -(M*N)
    for i in range(N):
        num_sum += sum(visit[i])
        
    return num_sum

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    
    result = 0
    land = []
    water = []
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'L':
                land.append((i, j, 0))
            elif field[i][j] == 'W':
                water.append((i, j, 1))
    
    if len(water) == 1:
        result = bfs(water[0])
    else:
        for i in range(len(land)):
            result += bfs(land[i])
    
    print(f'#{tc} {result}')