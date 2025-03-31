'''
D4 1868 파핑파핑 지뢰찾기

R x C 크기의 표를 이용한 게임이 있음.
표의 각 칸에는 지뢰가 있을 수도 있고 없을 수도 있음
표의 각 칸을 클릭했을 때, 그 칸이 지뢰가 있는 칸이면 '파핑파핑!'이라는 소리와 함께 게임이 끝남.
지뢰가 없는 칸이라면 변이 맞닿아 있거나, 꼭짓접이 맞닿아있는 최대 8칸에 대해 몇 개의 지뢰가 있는지가 0에서 8사이의 숫자로 클릭한 칸에 표시됨
만약 0이라면 8방향에 지뢰가 없다는것이 확정이기 때문에 그 칸의 8방향의 칸도 자동으로 숫자를 표시해 줌.
실제 게임에서는 어떤 지뢰가 있는지 알 수 없지만, 이 문제에선 알 수 있음.
지뢰를 *로, 지뢰가 없는 칸을 .로, 클릭한 지뢰가 없는 칸을 c로 나타냄.

표의 크기와 표가 주어질 때, 지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면
최소 몇 번 클릭해야 하는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [0, 0, 1, -1, 1, 1, -1, -1]            # 8방향 델타
dj = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(s1, s2):                # bfs 활용
    q = deque()
    q.append((s1, s2))
    
    while q:
        target = q.popleft()        # 디큐
        mine = 0                    # 주변 지뢰 갯수
        
        for i in range(8):              # 8방향
            x = target[0] + di[i]
            y = target[1] + dj[i]
            
            if x < 0 or x >= N or y < 0 or y >= N:      # 범위 조건
                continue
            
            if game[x][y] == '*':       # 만약 주변에 지뢰가 있으면 지뢰 갯수 추가
                mine += 1
                
        if mine:                        # 주변에 지뢰가 있는 상태다!
            game[target[0]][target[1]] = mine       # 그냥 해당 위치에 지뢰 개수 넣어주고, 인큐하지않음.
        else:                           # 주변에 지뢰가 없다!
            game[target[0]][target[1]] = 0          # 0으로 해주고 주위 좌표 다시 인큐
            for i in range(8):
                x = target[0] + di[i]
                y = target[1] + dj[i]
                
                if x < 0 or x >= N or y < 0 or y >= N:
                    continue
                
                if visit[x][y]:                     # 만약 방문한 상태라면 넣지 않음
                    continue
                
                visit[x][y] = 1                     # 방문상태로 바꿔주고 인큐
                q.append((x, y))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    result = 0
    
    for i in range(N):                      # 클릭하는 곳도 조건이 필요함. 최소 클릭 횟수 구하는 것이므로 퍼져나갈 수 있는 장소를 찾아서 클릭하는게 중요함.
        for j in range(N):
            if game[i][j] != '*' and visit[i][j] != 1:          # 지뢰가 있는곳이 아니고, 아직 누르지않은 버튼이라면 조건을 살펴보자!
                mine = 0
            
                for k in range(8):      # 주위에 지뢰가 하나도 없어야 우선순위로 누를수 있다!
                    x = i + di[k]
                    y = j + dj[k]
                    
                    if x < 0 or x >= N or y < 0 or y >= N:
                        continue
                    
                    if game[x][y] == '*':
                        mine += 1
                        
                if mine:            # 지뢰가 주변에 존재하면, 퍼져나갈 가능성 없으므로 다음 대상 탐색
                    continue
                else:               # 지뢰가 주변에 없으면 퍼져나갈 수 있다! bfs 함수에 해당 위치 넣고 실행!
                    bfs(i, j)
                    result += 1     # 클릭 한번 추가!
    
    for i in range(N):              # 퍼져나갈 수 있는 곳 모두 클릭한 뒤는 나머지 자잘한 클릭이 필요.
        for j in range(N):
            if game[i][j] == '.':   # 남은 버튼들 모두 일일이 클릭
                result += 1
    
    print(f'#{tc} {result}')