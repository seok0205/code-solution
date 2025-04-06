'''
G1 13460 구슬 탈출 2

직사각형 보드에 빨간 구슬, 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼는 게임

보드 세로는 N, 가로는 M. 1x1 칸으로 나누어져 있음
가장 바깥 행과 열은 모두 막혀있고, 보드에는 구멍이 하나 있음.
구슬들은 칸에 딱 알맞은 크기.
파란 구슬이 구멍에 들어가면 안됨

중력을 이용해 구슬을 굴려야하는데, 왼쪽, 오른쪽, 위쪽, 아래쪽으로 기울일 수 있음
각각 동작에서 공은 동시에 움직임. 빨간 구슬이 구멍에 빠지면 성공, 파란 구슬이 빠지면 실패.
동시에 빠져도 실패. 빨간 구슬, 파란 구슬은 동시에 같은 칸에 있지 못함.
기울이는 동작을 그만하는건 더 이상 구슬이 움직이지 않을 때 까지.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 문제
만약 10번 이하로 움직여 빨간 구슬을 못 뺀다면 -1 출력

입력:
N, M : 세로, 가로
N줄 동안 보드의 상태 :
'.' : 빈 칸
'#' : 장애물 or 벽
'O' : 구멍의 위치
'R' : 빨간 구슬 위치
'B' : 파란 구슬 위치
'''

import sys
sys.stdin = open('tc.txt', 'r')

def reverse_board(board):
    return [list(reversed(i)) for i in board]


def turn_left(board):
    return list(map(list, list(zip(*list(board[i][::-1] for i in range(N))))))


def turn_right(board):
    return list(map(list, list(zip(*list(board[::-1][i] for i in range(N))))))


def tilt(board):
    board_copy = [i[:] for i in board]
    
    for i in range(N):
        for j in range(M-1):
            if board_copy[i][j] == 'B':
                move = 0
                for k in range(j-1, 0, -1):
                    if board_copy[i][k] == 'O':
                        return board_copy, 2
                    if board_copy[i][k] in ['#', 'R']:
                        break
                    if board_copy[i][k] == '.':
                        move += 1
                board_copy[i][j], board_copy[i][j-move] = board_copy[i][j-move], board_copy[i][j]
            
            if board_copy[i][j] == 'R':
                move = 0
                for k in range(j-1, 0, -1):
                    if board_copy[i][k] == 'O':
                        return board_copy, 1
                    if board_copy[i][k] in ['#', 'B']:
                        break
                    if board_copy[i][k] == '.':
                        move += 1
                board_copy[i][j], board_copy[i][j-move] = board_copy[i][j-move], board_copy[i][j]

    return board_copy, 0

def game(board, direction, cnt, color):
    global result
    
    if cnt > result:
        return
    
    if cnt > 10:
        return
    
    if color == 1:
        result = min(result, cnt)
        return

    if color == 2:
        return
    
    board_copy = [i[:] for i in board]
    
    if direction == 'L':
        new_board, color = tilt(board_copy)
    elif direction == 'R':
        new_board, color = tilt(reverse_board(board_copy))
        new_board = reverse_board(new_board)
    elif direction == 'U':
        new_board, color = tilt(turn_left(board_copy))
        new_board = turn_right(new_board)
    elif direction == 'D':
        new_board, color = tilt(turn_right(board_copy))
        new_board = turn_left(new_board)
        
    game(new_board, 'L', cnt + 1, color)
    game(new_board, 'R', cnt + 1, color)
    game(new_board, 'U', cnt + 1, color)
    game(new_board, 'D', cnt + 1, color)

    
N, M = map(int, input().split())
main_board = [list(input()) for _ in range(N)]
result = float('inf')

game(main_board, 'L', 0, 0)
game(main_board, 'R', 0, 0)
game(main_board, 'U', 0, 0)
game(main_board, 'D', 0, 0)

if result == 'inf':
    print(-1)
else:  
    print(result)