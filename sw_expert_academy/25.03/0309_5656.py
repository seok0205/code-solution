'''
모의 SW 역량테스트 5656 벽돌 깨기

구슬을 쏘아 벽돌을 깨뜨리는 게임
구슬은 N번 쏠수 있고, 벽돌은 WxH 배열로 주어짐

규칙:
1. 구슬은 좌, 우로만 움직일 수 있어 항상 맨 위에 있는 벽돌만 깨뜨릴 수 있음
2. 벽돌은 숫자 1~9로 표현, 구슬이 명중한 벽돌은 상하좌우(벽돌에 적힌 숫자 - 1)칸 만큼 같이 제거

주어진 구슬을 N번 쐈을때, 남은 벽돌의 개수를 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    result = 0
    sub_bricks = [arr[:] for arr in bricks]
    stack = []
    
    for _ in range(N):
        can_break = []
        for i in range(W):
            for j in range(H):
                if sub_bricks[i][j]:
                    can_break.append((i, j))
                    break
    
        if sub_bricks[j][i]:
            visit = [[0] * W for _ in range(H)]
            boom = 0
            q = deque()
            q.append((j, i))
            
            while q:
                target = q.popleft()
                visit[target[0]][target[1]] = 1
                
                if sub_bricks[target[0]][target[1]] > 1:
                    for k in range(1, sub_bricks[j][i]):
                        for m in range(4):
                            x = j + (di[m] * k)
                            y = i + (dj[m] * k)
                            if 0 <= x < H and 0 <= y < W and sub_bricks[x][y] and visit[x][y] == 0:
                                q.append((x, y))
                                visit[x][y] = 1
    
            for l in range(H):
                boom += visit[l].count(1)
                
            for a in range(H):
                for b in range(W):
                    if visit[a][b]:
                        idx = 1
                        while True:
                            x1 = a - idx
                            y1 = b
                            if 0 <= x1 < H and 0 <= y1 < W and sub_bricks[x1][y1]:
                                sub_bricks[x1+1][y1] = sub_bricks[x1][y1]
                            else:
                                break
                            idx += 1
                                
            break
    
    print(f'#{tc} {result}')