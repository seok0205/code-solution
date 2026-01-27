'''
S2 21736 헌내기는 친구가 필요해

문제 설명:
NxM 크기 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동
예로, x,y에 있으면 상하좌우로만 갈수 있음.
캠퍼스 밖은 불가능.
만날 수 있는 사람의 수를 출력

입력:
두 정수 N, M 각각 1~600
둘째 줄부터 N개의 줄에는 캠퍼스 정보, o는 빈공간, x는 벽, i는 도연, p는 사람.

출력:
도연이가 만날 수 있는 사람의 수 출력.
아무도 못만나면 TT 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().strip().split())
campus = [list(map(str, input().strip())) for _ in range(N)]

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            me = (i, j)
            break

q = deque([me])
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[me[0]][me[1]] = 1
result = 0

while q:
    now = q.popleft()

    for i in range(4):
        nx = now[0] + x[i]
        ny = now[1] + y[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if visit[nx][ny] or campus[nx][ny] == 'X':
            continue

        if campus[nx][ny] in ['O', 'P']:
            q.append((nx, ny))
            visit[nx][ny] = 1
            
            if campus[nx][ny] == 'P':
                result += 1
        
if result:
    output(str(result))
else:
    output('TT')