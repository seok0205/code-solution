'''
S4 20125 쿠키의 신체 측정

문제 설명:
쿠키의 팔 다리 길이가 임의적으로 변하는 문제가 있음.
쿠키들의 신체 측정 하려고 함.
한변의 길이가 N인 정사각형 판 위에 누워 있는 쿠키.
어느 신체 부위도 판 밖으로 벗어나지 않음.
판의 x번째 행, y번째 열에 위치한 곳을 (x, y)라 정의.
판의 맨 왼쪽 위칸을 (1,1), 오른쪽 아래 칸을 (N,N)으로 정의.
머리, 심장, 허리, 팔, 다리로 구성되어 있음.
머리는 심장 위 바로 윗 칸에 1칸 크기.
왼쪽 팔은 심장의 왼쪽으로 뻗어있고 오른쪽 팔은 오른쪽으로 뻗어있음.
허리는 심장의 바로 아래 쪽에 붙어있고, 아래쪽으로 뻗어있음.
각 다리들도 허리의 왼쪽아래, 오른쪽아래에 붙어있고, 다 아래쪽으로 뻗어있음.
각 신체 부위들은 절대로 끊겨있지 않으며 굽혀진 곳도 없음.
또한, 허리, 팔, 다리의 길이는 1이상이고, 너비는 무조건 1.
쿠키의 신체가 주어질 때, 심장의 위치와 팔, 다리, 허리 길이를 구하는 문제.

출력:
첫번째 줄에 심장이 위치한 행의 번호 x, 열의 번호 y 출력. 공백 두고.
두번째 줄에 각각 왼쪽팔, 오른쪽팔, 허리, 왼쪽다리, 오른쪽다리 길이를 출력.

제한:
5 <= N <= 1000, N은 한변의 길이 의미
* 혹은 _로 신체 부분이 표현됨. *이 신체부위, _는 빈 공간.
쿠키의 신체 조건에 위배된 조건은 없음.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
boards = [list(input().strip()) for _ in range(N)]

hearts_find = False
for i in range(N):
    if hearts_find:
        break
    for j in range(N):
        if boards[i][j] == '*':
            hearts_find = True
            hearts = (i+1, j)
            break

result = [0, 0, 0, 0, 0]

for i in range(hearts[1]-1, -1, -1):
    if boards[hearts[0]][i] == '*':
        result[0] += 1
    else:
        break

for i in range(hearts[1]+1, N):
    if boards[hearts[0]][i] == '*':
        result[1] += 1
    else:
        break

for i in range(hearts[0]+1, N):
    if boards[i][hearts[1]] == '*':
        result[2] += 1
    else:
        heap = (i-1, hearts[1])
        break

for i in range(heap[0]+1, N):
    if boards[i][heap[1]-1] == '*':
        result[3] += 1
    else:
        break

for i in range(heap[0]+1, N):
    if boards[i][heap[1]+1] == '*':
        result[4] += 1
    else:
        break

print(hearts[0]+1, hearts[1]+1)
print(' '.join(map(str, result)))