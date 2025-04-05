'''
G1 12100 2048(Easy)

nxn 크기 보드에서 하는 게임. 이 게임에서 한 번의 이동은 보드 위 전체 블록을
상하좌우 네 방향 중 하나로 이동시키는 것.
같은 값을 가진 블록이 충돌하면 하나로 합쳐짐.
한번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없음.(원래는 하나의 블록이 추가되지만 여긴 예외.)

똑같은 수가 세 개 있으면 이동하려는 쪽의 칸이 먼저 합쳐짐.
보드 크기, 보드판 블록이 주어지면, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 문제.

0은 빈칸이고, 이외의 값은 모두 블록임.
블록의 값은 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴. 블록은 적어도 하나 주어짐.
'''

import sys
sys.stdin = open('tc.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def func(direction):
    if direction == "L":
        for i in range(N):          # 행
            for j in range(N-1):        # 열
                if board[i][j]:         # 값이 있으면
                    for k in range(j+1, N):     # 0 제외한 가장 가까운 블록 확인
                        if board[i][k] == 0:
                            continue
                        
                        if board[i][j] == board[i][k]:
                            board[i][j] *= 2
                            board[i][k] = 0
                            break