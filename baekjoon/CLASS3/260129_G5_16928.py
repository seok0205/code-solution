'''
G5 16928 뱀과 사다리 게임

문제 설명:
주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면 최소 몇 번만에 도착점에 갈 수 있을까?
주사위는 1부터 6까지 하나씩 적혀있고, 보드판은 10x10이다.
1부터 100까지 적혀져 있다.
i번 칸에 있는 상태에서 주사위를 굴려 나온수만큼 i+n칸으로 이동해야함.
만약 주사위 굴린 결과가 100번을 넘어간다면 이동할 수 없음.
도착한 칸이 사다리라면, 사다리를 타고 위로 올라감. 뱀이 있으면 뱀을 따라 내려감.
즉, 사다리를 이용해 이동한 칸은 원래있던칸 번호보다 크고, 뱀이면 작아진다.
게임의 목표는 1번 칸에서 시작해 100번칸에 도착하는 것.
게임판 상태가 주어질 때, 100번 칸에 도착하기 위해 주사위를 굴려야하는 횟수의 최솟값 구하라.

입력:
첫째 줄에 게임판에 있는 사다리의 수 N(1~15)과 뱀의 수 M(1~15)가 주어짐.
둘째 줄부터 N개 줄에 사다리의 정보를 의미하는 x,y 주어짐. x칸에 도착하면 y칸으로 이동한다는 뜻.
다음 M개의 줄에는 u, v 주어짐. u칸에 도착하면 v칸으로 이동.
1번, 100번칸은 뱀과 사다리 시작 및 끝이 아님. 모든 칸은 최대 하나의 사다리 혹은 뱀을 가짐. 동시에 가지는 경우 없음. 항상 100번 칸에 도착 가능한 입력만 주어짐.

출력:
100번 칸에 도착하기 위해 굴려야하는 최소 횟수 출력
'''

import sys
from collections import deque
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().strip().split())
board = [0 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().strip().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().strip().split())
    board[u] = v


def solution():
    q = deque()
    visit = [0] * 101
    result = 100
    q.append((1, 0))
    visit[1] = 1

    while q:
        x, cnt = q.popleft()
        if x == 100:
            result = min(result, cnt)

        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue

            if visit[nx]:
                continue

            visit[nx] = 1
            if board[nx]:
                q.append((board[nx], cnt + 1))
            else:
                q.append((nx, cnt + 1))

    output(str(result))


solution()