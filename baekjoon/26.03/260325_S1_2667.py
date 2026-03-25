'''
S1 2667 단지번호붙이기 복습

풀이 시간 : 21분 24초

문제 설명:
정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성.

입력:
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력.

출력:
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque

n = int(input())
homes = [list(map(int, input().strip())) for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(visit, a, b, cnt):
    q = deque([(a, b)])
    visit[a][b] = cnt
    
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and homes[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = cnt
    
    return visit


new_visit = [[0] * n for _ in range(n)]
new_cnt = 1

for i in range(n):
    for j in range(n):
        if homes[i][j] and new_visit[i][j] == 0:
            new_visit = bfs(new_visit, i, j, new_cnt)
            new_cnt += 1

print(new_cnt - 1)

result = []
for i in range(1, new_cnt):
    cnt = 0
    for row in new_visit:
        cnt += row.count(i)

    result.append(cnt)

result.sort()

for i in result:
    print(i)