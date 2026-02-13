'''
L3 퍼즐 조각 채우기

문제 설명:
테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. 게임 보드와 테이블은 모두 각 칸이 1x1 크기인 정사각 격자 모양입니다. 이때, 다음 규칙에 따라 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈칸에 채우면 됩니다.

조각은 한 번에 하나씩 채워 넣습니다.
조각을 회전시킬 수 있습니다.
조각을 뒤집을 수는 없습니다.
게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.

현재 게임 보드의 상태 game_board, 테이블 위에 놓인 퍼즐 조각의 상태 table이 매개변수로 주어집니다. 규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 return 하도록 solution 함수를 완성해주세요.

제약:
3 ≤ game_board의 행 길이 ≤ 50
game_board의 각 열 길이 = game_board의 행 길이
즉, 게임 보드는 정사각 격자 모양입니다.
game_board의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 이미 채워진 칸을 나타냅니다.
퍼즐 조각이 놓일 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
table의 행 길이 = game_board의 행 길이
table의 각 열 길이 = table의 행 길이
즉, 테이블은 game_board와 같은 크기의 정사각 격자 모양입니다.
table의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 조각이 놓인 칸을 나타냅니다.
퍼즐 조각은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
game_board에는 반드시 하나 이상의 빈칸이 있습니다.
table에는 반드시 하나 이상의 블록이 놓여 있습니다.
'''

from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    
    def find_blocks(field, target):
        blocks = []
        visit = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if field[i][j] == target and not visit[i][j]:
                    q = deque([(i, j)])
                    visit[i][j] = 1
                    block = []
                    
                    while q:
                        x, y = q.popleft()
                        block.append([x, y])
                        
                        for k in range(4):
                            nx = x + di[k]
                            ny = y + dj[k]
                            
                            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                                continue
                            
                            if visit[nx][ny] or field[nx][ny] != target:
                                continue
                                
                            visit[nx][ny] = 1
                            q.append((nx, ny))
                        
                        min_a = min(s[0] for s in block)
                        min_b = min(s[1] for s in block)
                        new_block = sorted([[s[0]-min_a, s[1]-min_b] for s in block])
                    blocks.append(new_block)
        return blocks    
    
    blocks = find_blocks(table, 1)
    boards = find_blocks(game_board, 0)
    
    def rotate(block):
        rotated = [[s[1], -s[0]] for s in block]
        min_a = min(s[0] for s in rotated)
        min_b = min(s[1] for s in rotated)
        return sorted([[s[0]-min_a, s[1]-min_b] for s in rotated])
    
    answer = 0
    visit = [0] * len(blocks)
    
    for board in boards:
        found = False
        idx = -1
        for block in blocks:
            idx += 1
            if visit[idx]:
                continue
            if len(board) != len(block):
                continue
            
            temp = block
            for _ in range(4):
                if board == temp:
                    answer += len(board)
                    visit[idx] = 1
                    found = True
                    break
                    
                temp = rotate(temp)
            if found:
                break
    
    return answer