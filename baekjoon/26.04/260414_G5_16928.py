'''
G5 16928 뱀과 사다리 게임 (재풀이)

문제 설명:
주사위를 조작해 내가 원하는 수가 나오게 만들 수 있으면, 최소 몇 번만에 도착점에 도착할 수 있나?

게임은 정육면체 주사위 사용, 1부터 6이 각 면에 적힘.
게임 크기는 10x10, 100개 칸 보드판. 1부터 100까지 수가 하나씩 순서대로 적힘.

주사위를 굴려 나온 수만큼 이동. 플레이어가 i번 칸에 있고, 주사위 굴려 4가 나오면 i+4로 이동.

만약 100 넘어가면 이동 못함. 도착한 곳이 사다리칸이면 타고 위로 올라감.
뱀 칸에 도착하면 뱀 따라서 내려감.

사다리는 이동 시 원래 칸 보다 크고, 뱀은 작은 곳에 도착.

목표는 1번부터 시작해 100번 칸에 도착하는 것.
주사위 굴리는 횟수의 최솟값을 구해라.

입력:
첫째 줄 - N, M (1 <= N <= 15, 1 <= M <= 15)
둘째 줄부터 N개 줄 - 사다리 정보 x, y (x < y)
x에 도착하면 y로 간다는 뜻
다음 M개 줄 - 뱀 정보 u, v (u > v) u -> v.
1번칸 100번칸은 뱀, 사다리 아님. 한칸이 동시에 둘다 못가짐.
항상 100번칸에 갈수 있는 입력만 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
boards = [0] * 101

for _ in range(N):
    x, y = map(int, input().split())
    boards[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    boards[u] = v

q = deque([(1, 0)])
visit = [0] * 101
visit[1] = 1
result = 100

while q:
    x, cnt = q.popleft()

    if x == 100:
        result = min(result, cnt)
        break
    
    for i in range(1, 7):
        nx = x + i

        if nx > 100:
            continue

        if visit[nx]:
            continue
        
        visit[nx] = 1
        if boards[nx]:
            q.append((boards[nx], cnt + 1))
        else:
            q.append((nx, cnt + 1))

print(result)