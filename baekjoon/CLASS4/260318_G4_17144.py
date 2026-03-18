'''
G4 17144 미세먼지 안녕!

문제 설명:
미세먼지 제거하기 위해 공기청정기 설치하려함.
RxC인 격자판위에 1x1 크기의 칸으로 나눔.
(r, c)는 r행 c열 의미.
공기청정기는 항상 1번열에 설치. 크기는 두 행을 차지.
(r, c)에 있는 미세먼지 양은 A.
1초동안 아래의 일이 일어남.
1. 미세먼지 확산. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어남.
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
    (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋x(확산된 방향의 개수) 이다.
2. 공기청정기 작동.
    공기청정기에서는 바람이 나온다.
    위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

방의 정보가 주어질 때, T초가 지난 후 방에 남은 미세먼지 양을 구하는 문제.

입력:
첫째 줄 - R, C, T (6 <= R, C <= 50, 1 <= T <= 1,000)
둘째 줄부터 R개의 줄 - A(-1 <= A <= 1,000).
공기청정기가 설치된 곳은 A가 -1이고, 나머지 값은 미세먼지 양.
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있음.

출력:
첫째 줄에 T초가 지난 후 방에 남아있는 미세먼지의 양을 출력.
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
cleaners = []

for i in range(R):
    if room[i][0] == -1:
        cleaners.append(i)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(T):
    visit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] == 0 or room[i][j] == -1:
                continue
            
            temp = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if ni < 0 or ni >= R or nj < 0 or nj >= C:
                    continue

                if room[ni][nj] == -1:
                    continue

                visit[ni][nj] += room[i][j] // 5
                temp += 1
            
            room[i][j] -= temp * (room[i][j] // 5)

    for i in range(R):
        for j in range(C):
            room[i][j] += visit[i][j]

    up = cleaners[0]

    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]
    room[0][:C-1] = room[0][1:]
    for i in range(up):
        room[i][C-1] = room[i+1][C-1]
    room[up][2:] = room[up][1:C-1]
    room[up][1] = 0

    down = cleaners[1]

    for i in range(down+1, R-1):
        room[i][0] = room[i+1][0]
    room[R-1][:C-1] = room[R-1][1:]
    for i in range(R-1, down, -1):
        room[i][C-1] = room[i-1][C-1]
    room[down][2:] = room[down][1:C-1]
    room[down][1] = 0

result = sum(sum(row) for row in room) + 2
output(str(result))


# python 전용

import sys

# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

up = -1
down = -1
for i in range(R):
    if room[i][0] == -1:
        up = i
        down = i + 1
        break

for _ in range(T):
    added_dust = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] >= 5:
                amount = room[r][c] // 5

                if r > 0 and room[r-1][c] != -1:
                    added_dust[r-1][c] += amount
                    room[r][c] -= amount
                
                if r < R - 1 and room[r+1][c] != -1:
                    added_dust[r+1][c] += amount
                    room[r][c] -= amount
                
                if c > 0 and room[r][c-1] != -1:
                    added_dust[r][c-1] += amount
                    room[r][c] -= amount
                
                if c < C - 1 and room[r][c+1] != -1:
                    added_dust[r][c+1] += amount
                    room[r][c] -= amount
    
    for r in range(R):
        for c in range(C):
            room[r][c] += added_dust[r][c]

    for i in range(up - 1, 0, -1): room[i][0] = room[i-1][0]
    room[0][:C-1] = room[0][1:]
    for i in range(up): room[i][C-1] = room[i+1][C-1]
    room[up][2:] = room[up][1:C-1]
    room[up][1] = 0

    for i in range(down + 1, R - 1): room[i][0] = room[i+1][0]
    room[R-1][:C-1] = room[R-1][1:]
    for i in range(R - 1, down, -1): room[i][C-1] = room[i-1][C-1]
    room[down][2:] = room[down][1:C-1]
    room[down][1] = 0

ans = sum(map(sum, room)) + 2
print(ans)