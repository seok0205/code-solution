'''
G5 7569 토마토

문제 설명:
토마토 농장에선 토마토를 보관하는 큰 창고를 가지고 있음.
토마토들 중엔 익은 것도, 안 익은 것도 있음.
보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 것들의 영향을 받아 익게 됨.
인접한 곳은 해당 토마토의 상하좌우앞뒤 여섯 방향의 토마토 의미.
대각선에는 영향 못줌. 혼자 익는 경우는 없음.
며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 함.
상자의 일부 칸에는 토마토 없을 수도 있음.

입력:
첫 줄 - M, N (2~100), H(1~100)
둘째 줄부터 N개의 줄에 하나의 상자에 담긴 토마토 정보(M개의 정수가 N개의 줄동안).
정수 1은 익은 토마토, 0은 안익은것, -1은 토마토 없는 자리 의미.
이런 N개 줄이 H번 반복해서 주어짐.

출력:
토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력.
저장될 때부터 모든 토마토가 익어있는 상태면 0 출력.
토마토가 모두 익지 못하는 상황이면 -1 출력.
'''

import sys
from collections import deque
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

M, N, H = map(int, input().strip().split())
boxes = []

for _ in range(H):
    box = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        box.append(row)
    boxes.append(box)

xi = [0, 0, 1, -1, 0, 0]
xj = [1, -1, 0, 0, 0, 0]
xh = [0, 0, 0, 0, 1, -1]

q = deque()
cnt = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))
            if boxes[i][j][k] == 0:
                cnt += 1

while q:
    h, x, y = q.popleft()
    result = boxes[h][x][y]
    
    for dir in range(6):
        nx = x + xi[dir]
        ny = y + xj[dir]
        nh = h + xh[dir]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or nh < 0 or nh >= H:
            continue
        
        if boxes[nh][nx][ny]:
            continue

        if boxes[nh][nx][ny] == -1:
            continue
        
        boxes[nh][nx][ny] = boxes[h][x][y] + 1
        cnt -= 1
        q.append((nh, nx, ny))

if cnt == 0:
    output(str(result-1))
else:
    output('-1')