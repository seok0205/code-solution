'''
L3 아이템 줍기

문제 설명:
지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.
즉, 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
지형이 2개 이상으로 분리된 경우도 없습니다.
한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

제약:
rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    rec_field = [[-1] * 102 for _ in range(102)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    rec_field[i][j] = 0
                elif rec_field[i][j] != 0:
                    rec_field[i][j] = 1
    
    
    def bfs(c1, c2, i1, i2):
        nonlocal answer
        
        di = [0, 0, -1, 1]
        dj = [1, -1, 0, 0]
        
        q = deque()
        q.append((c1*2, c2*2))
        visit = [[0] * 102 for _ in range(102)]
        visit[c1*2][c2*2] = 1
        
        while q:
            x, y = q.popleft()
            
            if x == i1*2 and y == i2*2:
                    answer = visit[x][y]
                    return
            
            for k in range(4):
                nx = x + di[k]
                ny = y + dj[k]
                
                if nx < 0 or nx >= 102 or ny < 0 or ny >= 102:
                    continue
                    
                if visit[nx][ny]:
                    continue
                    
                if rec_field[nx][ny] != 1:
                    continue
                    
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    
    
    bfs(characterX, characterY, itemX, itemY)
    return answer // 2