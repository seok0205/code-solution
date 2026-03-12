'''
1987 G4 알파벳

문제 설명:
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있음.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열)에는 말이 놓임.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 함.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없음.
좌측 상단에서 시작해 말이 최대한 몇 칸 지날 수 있는지 구하는 문제.
말이 지나는 칸은 좌측 상단의 칸도 포함.

입력:
첫줄에 R, C가 공백을 두고 주어짐. 각각 1보다 크거나 같고 20보다 작거나 같음.
둘째 줄부터 R개의 줄에 걸쳐 C개의 알파벳 빈칸 없이 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

r, c = map(int, input().split())
board = []

for _ in range(r):
    data = list(map(str, input().strip()))
    board.append(data)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

q = set([(0, 0, board[0][0])])
result = 1

while q:
    x, y, record = q.pop()
    result = max(result, len(record))

    if result == 26:
        break

    for i in range(4):
        nx = x + di[i]
        ny = y + dj[i]

        if 0 > nx or nx >= r or ny < 0 or ny >= c:
            continue

        if board[nx][ny] in record:
            continue

        q.add((nx, ny, record + board[nx][ny]))

output(str(result))