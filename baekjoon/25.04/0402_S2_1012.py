'''
1012 S2 유기농 배추

해충 방지에 효과적인 지렁이 구입.
배추 근처에 서식하며 해충을 잡아먹어서 배추 보호.
특히, 어떤 배추에 배추흰지렁이가 한 마리랄도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동 가능,
그 배추들 역시 보호받음. 
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것임.

배추를 재배하는 땅은 고르지 못해 군데군데 심어놓음.
배추들이 모여있는 곳에는 배추 흰 지렁이가 한마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지
조사하면 총 몇 마리의 지렁이가 필요한지 알수 있음

0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는땅.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(s1, s2):
    q = deque()
    q.append((s1, s2))
    field[s1][s2] = 0
    
    while q:
        target = q.popleft()
        for k in range(4):
            x = target[0] + di[k]
            y = target[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= M:      # 범위 이탈
                continue
            
            if field[x][y] == 0:        # 배추없으면 다음 자리 탐색
                continue
            
            field[x][y] = 0     # 보호받았으므로 표시
            q.append((x, y))


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    result = 0
    
    for _ in range(K):
        a, b = map(int, input().split())
        field[b][a] = 1             # 해당 좌표에 배추 심기
        
    for i in range(N):              # 지렁이가 배추하나 발견하면 그 범위내 배추들 모두 보호.
        for j in range(M):
            if field[i][j]:
                bfs(i, j)           # 배추하나 발견하고 모두 보호하면, 보호당한 배추들은 field내에서 0으로 변함. 즉, 한번 보호받으면 다음 반복에선 걸리지 않음.
                result += 1         # 결과하나 증가
                
    print(result)