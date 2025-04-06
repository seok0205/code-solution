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

def func(board):
    board_copy = [i[:] for i in board]
    
    for i in range(N):          # 행
        for j in range(N-1):        # 열
            if board_copy[i][j]:         # 값이 0이 아니면
                for k in range(j+1, N):     # 0 제외한 가장 가까운 블록 확인
                    if board_copy[i][k] == 0:       # 0이면 건너뛰고
                        continue
                    
                    if board_copy[i][j] == board_copy[i][k]:        # 같은 숫자면 두 블록 합치기
                        board_copy[i][j] *= 2                       # 같은 숫자이므로 곱하기 2
                        board_copy[i][k] = 0                        # 합친 숫자 블록은 0으로 변환
                        break                                       # 한턴에 한번 합칠 수 있으므로 다음 합칠 블록 찾으러 넘어감
                    else:
                        break
    
    for x in range(N):                                          # 숫자 블록 왼쪽으로 밀기
        for y in range(N-1):
            if board_copy[x][y] == 0:                           # 왼쪽부터 탐색하고 0이 나오면 뒤에 바로 나오는 숫자와 자리 바꿈. 반복하면 왼쪽으로 숫자 모두 밀기 가능
                for a in range(y+1, N):
                    if board_copy[x][a]:
                        board_copy[x][y], board_copy[x][a] = board_copy[x][a], board_copy[x][y]
                        break
    
    return board_copy
    
    
def reverse_board(board):           # 오른쪽으로 움직일 때,
    board_copy = [list(reversed(i)) for i in board]
    return board_copy


def turn_right(board):              # 아래로 밀려면 보드를 오른쪽으로 돌리고 func() 실행
    board_copy = list(map(list, zip(*list(board[::-1][i] for i in range(N)))))
    return board_copy


def turn_left(board):               # 위로 밀려면 보드를 왼쪽으로 돌리고 func() 실행
    board_copy = list(map(list, zip(*list(board[i][::-1] for i in range(N)))))
    return board_copy


def play(board, direction, cnt):
    global max_block
    
    if cnt == 5:                        # 5번 밀었으면 보드의 최댓값 가진 블록 확인
        for i in range(N):
            for j in range(N):
                max_block = max(max_block, board[i][j])
                
        return
    
    board_copy = [i[:] for i in board]      # 깊은 복사
    
    if direction == "L":                    # 왼쪽으로 밀려면 그대로 func() 실행
        board_copy = func(board_copy)
    elif direction == "R":                  # 오른쪽으로 밀려면 보드를 뒤집고 func()실행, 밀었다면 다시 원상태 복귀시켜줌
        board_copy = reverse_board(func(reverse_board(board_copy)))
    elif direction == "U":                  # 위로 밀려면 보드를 왼쪽으로 돌리고 밀고, 다시 오른쪽으로 돌려서 보드를 원상태로 돌려놓기
        board_copy = turn_right(func(turn_left(board_copy)))
    elif direction == "D":                  # 아래로 밀려면 보드를 오른쪽으로 돌리고 밀고, 다시 왼쪽으로 돌려 보드를 원상태로 복구
        board_copy = turn_left(func(turn_right(board_copy)))
        
    play(board_copy, "L", cnt + 1)      # 재귀 실행하여 모든 경우의 수 체크
    play(board_copy, "R", cnt + 1)
    play(board_copy, "U", cnt + 1)
    play(board_copy, "D", cnt + 1)
    
    
N = int(input())
main_board = [list(map(int, input().split())) for _ in range(N)]
max_block = 0

play(main_board, "L", 0)            # 첫턴은 왼쪽 밀기 시작
play(main_board, "R", 0)            # 오른쪽 밀기부터 시작
play(main_board, "U", 0)            # 위로 밀기부터 시작
play(main_board, "D", 0)            # 아래로 밀기부터 시작

print(max_block)