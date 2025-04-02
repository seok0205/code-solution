'''
S2 3085 사탕 게임

NxN 크기에 사탕을 채워 놓음. 사탕의 색은 모두 같지 않을 수 있음.
사탕의 색이 다른 인접한 두 칸을 고름. 그 다음 고른 칸에 들어있는 사탕을 서로 교환.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)을 고른 다음 그 사탕을 모두 먹음

사탕이 채워진 상태가 주어졌을 때, 먹을 수 있는 사탕의 최대 개수를 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')

N = int(input())
candy = [list(input()) for _ in range(N)]
result = 0

di = [0, 1]
dj = [1, 0]

for i in range(N):
    for j in range(N):
        target = (i, j)
        for k in range(2):
            x = target[0] + di[k]
            y = target[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            
            if candy[target[0]][target[1]] == candy[x][y]:
                continue
            
            candy[x][y], candy[target[0]][target[1]] = candy[target[0]][target[1]], candy[x][y]
            
            
            
            candy[x][y], candy[target[0]][target[1]] = candy[target[0]][target[1]], candy[x][y]