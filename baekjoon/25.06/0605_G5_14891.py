'''
G5 14891 톱니바퀴

4개의 톱니바퀴가 일렬로 놓아져있음.
K번 회전시키려고함. 한칸 기준으로 회전함. 시계방향, 반시계방향 회전 존재.
회전시키려면 서로 맞닿은 극에 따라 달라짐. 특정 톱니바퀴 회전시키면, 그 옆의 톱니바퀴와
서로 맞닿은 극이 다르면 옆의 톱니바퀴는 특정 톱니바퀴가 회전한 반대방향으로 회전함.

하지만 같은 극이라면, 옆 톱니바퀴는 회전하지 않음.

초기 톱니바퀴 상태와, 톱니바퀴 회전 수가 주어질 때, 최종 톱니바퀴 상태 구하는 문제

입력:
첫 줄부터 네번째 줄까지 1번부터 4번 톱니바퀴 상태 주어짐(0은 N극, 1은 S극)
다섯째줄엔 K
그다음 줄부터 K줄동안 회전시킬 방법 주어짐(두개의 정수, 번호와 방향(1은 시계, -1은 반시계))

출력:
K번 회전 후 톱니바퀴 상태따라 점수 합 출력.
각 톱니바퀴의 12시방향 톱니가 N극이면 0점. S극이면 번호순서대로 (1, 2, 4, 8)점.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def make_operation_list(wheel_num, direction):      # 선택 톱니바퀴 기준 돌아갈 톱니바퀴를 리스트로 판별
    new_list = [0, 0, 0, 0]     # 0에서 -1이나 1로 바뀌지 않으면 안돌아감

    if wheel_num == 0:          # 맨 왼쪽(1번) 톱니바퀴 기준
        new_list[0] = direction     # 기준점은 무조건 회전.
        for i in range(3):          # 퍼져나가면서 회전할지 안할지 판별
            if wheels[i][2] != wheels[i+1][6]:
                if i%2 == 0:
                    new_list[i+1] = -direction
                else:
                    new_list[i+1] = direction
            else:                   # 퍼져나가지 못하면 그대로 구문탈출
                break

    elif wheel_num == 3:        # 맨 오른쪽(4번) 톱니바퀴 기준
        new_list[3] = direction
        for i in range(3, 0, -1):
            if wheels[i][6] != wheels[i-1][2]:
                if i%2:
                    new_list[i-1] = -direction
                else:
                    new_list[i-1] = direction
            else:
                break
    
    else:                       # 2번 3번은 양쪽으로 퍼져나가면서 판별
        if wheel_num == 1:      # 2번, 3번일 때 a, b 값이 달라야함. 2번 톱니는 왼쪽에 하나 오른쪽 둘의 톱니가 존재. 3번은 개수가 반대.
            new_list[1] = direction
            a, b = 2, 1
        elif wheel_num == 2:
            new_list[2] = direction
            a, b = 1, 2

        for i in range(a):              # 왼쪽 오른쪽 판별.
            if wheels[wheel_num+i][2] != wheels[wheel_num+i+1][6]:
                if i%2:
                    new_list[wheel_num+i+1] = direction
                else:
                    new_list[wheel_num+i+1] = -direction
            else:
                break

        for i in range(b):        
            if wheels[wheel_num-i][6] != wheels[wheel_num-i-1][2]:
                if i%2:
                    new_list[wheel_num-i-1] = direction
                else:
                    new_list[wheel_num-i-1] = -direction
            else:
                break

    return new_list     # 돌아갈 톱니바퀴(방향)을 담은 리스트 반환


def turn(operation_list):
    for i in range(4):      # 리스트에 돌아갈 톱니 방향 담겨있으므로 그대로 순회하면서 돌리면 됨
        if operation_list[i]:
            if operation_list[i] == 1:      # 시계방향
                a = wheels[i].pop()
                wheels[i].insert(0, a)
            elif operation_list[i] == -1:   # 반시계 방향
                a = wheels[i].pop(0)
                wheels[i].append(a)
            else:
                continue


wheels = [list(map(int, list(input().strip()))) for _ in range(4)]
K = int(input())

for _ in range(K):
    wheel_num, direction = map(int, input().split())
    operation_list = make_operation_list(wheel_num-1, direction)
    turn(operation_list)

result = 0
for i in range(4):      # 0번 인덱스에 톱니 12시방향의 극 있음. S극이면 해당 점수 추가.
    if wheels[i][0] == 1:
        result += 2**i

print(result)