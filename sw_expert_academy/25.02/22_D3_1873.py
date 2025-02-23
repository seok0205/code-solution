'''
D3 1873 상호의 배틀필드

문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.
 
문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

전차 이동시 게임 밖이면 이동 X
포탄 발사 시, 포탄은 벽돌이나 강철로 만들어진 벽에 충돌하거나 맵 밖으로 갈때까지 직진

포탄이 벽에 충돌하면 포탄은 소멸, 부딪힌 벽이 벽돌이라면 파괴 후 평지 변환
강철로 만들어진 벽에 포탄이 부딪히면 아무일도 안 일어남

맵밖으로 포탄이 이동 시 아무일도 안 일어남
초기맵 상태 및 사용자 입력이 주어질 때, 최종 게임 맵의 상태를 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')


def shoot(mobile, field):
    move_dic = {'<': (1, 0), '>': (0, 1), '^': (-1, 0), 'v': (0,-1)}     # 이동 방향
    
    direction = move_dic[mobile[0]]
    idx = 0

    x = mobile[1]   # 전차가 현재 존재하는 위치에서 포탄 발사하므로 전차의 위치가 포탄의 출발 지점
    y = mobile[2]
    while True:     # 델타 활용(move_dic 활용)
        idx += 1
        mx = x + direction[0] * idx
        my = y + direction[1] * idx
        if 0 <= mx < H and 0 <= my < W and field[mx][my] == "*":        # 벽돌로 지어진 벽 만나면 파괴
            field[mx][my] = "."
            break
        elif 0 <= mx < H and 0 <= my < W and field[mx][my] == "#":      # 강철 벽 만나면 부수지 못함
            break
        elif 0 > mx or mx >= H or 0 > my or my >= H:
            break
    
    return field        # 포탄의 턴 한번 도출


def move(mobile, c):
    x = mobile[1]
    y = mobile[2]
    if c == 'U': 
        if 0 <= x < H and 0 <= y < H and battle_field[x][y] not in '-*#':
            battle_field[mobile[1]][mobile[2]] = '.'
            mobile[1] = x
            mobile[0] = '^'
            battle_field[mobile[1]][mobile[2]] = mobile[0]
    elif c == 'D':
        battle_field[mobile[1]][mobile[2]] = '.'
        mobile[1] += mobile[1] + 1
        mobile[0] = 'v'
        battle_field[mobile[1]][mobile[2]] = mobile[0]
    elif c == 'L':
        battle_field[mobile[1]][mobile[2]] = '.'
        mobile[2] = mobile[2] - 1
        mobile[0] = '<'
        battle_field[mobile[1]][mobile[2]] = mobile[0]
    elif c == 'R':
        battle_field[mobile[1]][mobile[2]] = '.'
        mobile[2] = mobile[2] + 1
        mobile[0] = '>'
        battle_field[mobile[1]][mobile[2]] = mobile[0]
    
    return mobile


T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    battle_field = [list(input()) for _ in range(H)]
    N = int(input())
    command = input()

    for i in range(H):      # 탱크의 첫 위치 및 상태 탐색
        for j in range(W):
            if battle_field[i][j] in "><v^":
                tank = [battle_field[i][j], i, j]
                
    for i in command:
        if i == 'S':
            battle_field = shoot(tank, battle_field)
        elif i in "UDLR":
            tank = move(tank, i)
            
    print(battle_field)