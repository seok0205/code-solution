'''
G5 20055 컨베이어 벨트 위의 로봇

길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트 위아래로 감싸며 돌고 있음.
벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있으며, 각 칸에는 1부터 2N까지의 번호로 매겨져 있음.

벨트가 한 칸 회전하면 1번부터 2N-1까지의 칸은 다음 번호의 칸이 있는 위치로 이동, 2N칸은 1번칸으로 이동.
i번 칸 내구도는 A_i.
1번칸이 올리는 위치, N번칸이 내리는 위치.

박스 모양 로봇을 하나씩 올리려고 함. 로봇은 올리는 위치에만 올릴 수 있음.
언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내림.
로봇은 컨베이어 벨트 위에서 스스로 이동 가능.
로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸 내구도는 1 감소.

로봇들을 건너편으로 옮기는 과정에서 일어나는 일.
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동. 만약 이동 못하면 가만히.
- 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아 있어야 함.
3. 올리는 위치에 있는 칸의 내구도가 0이아니면 올리는 위치에 로봇 올림.
4. 내구도가 0인 칸의 개수가 K개 이상이면 종료. 아니면 1번으로 돌아감.

종료되었을 때, 몇 번째 단계까 진행 중이었는지 구하는 문제.
시작은 1단계.

입력:
첫째 줄 - N, K (2 <= N <= 100, 1 <= K <= 2N)
둘째 줄 - A_1 ~ A_2N (1 <= A_i <= 1,000)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * (N-1))
result = 1


def check(belt):
    if belt.count(0) >= K:
        return True
    else:
        return False


while True:
    belt.appendleft((belt.pop()))
    robots.pop()
    robots.appendleft(0)

    for i in range(N-2, 0, -1):
        if belt[i+1] and robots[i]:
            if i < N-2 and robots[i+1] == 0:
                robots[i] = 0
                robots[i+1] = 1
                belt[i+1] -= 1
            elif i == N-2:
                belt[i+1] -= 1
                robots[i] = 0

    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1
    
    if check(belt):
        break

    result += 1

print(result)