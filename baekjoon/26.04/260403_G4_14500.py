'''
G4 14500 테트로미노

문제 설명:
폴리오미노란 크기가 1x1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다.
즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 5가지가 있다.
크기가 NxM인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1x1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력:
첫 줄 - 세로 N, 가로 M (4 <= N, M <= 500)
둘째줄 부터 N개의 줄에 종이의 수. 입력은 1000넘지않는 자연수

출력:
테트로미노가 놓인 칸에 쓰인 수들 합의 최댓값 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
papers = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
seq = [(0, 0, 0), (0, 0, 1), (0, 0, 3), (0, 1, 0), (0, 3, 0), (0, 1, 2)]

def find(x, y):
    max_num = 0
    for i in range(6):
        a, b, c = seq[i]
        for j in range(4):
            temp = papers[x][y]
            na, nb, nc = (a+j)%4, (b+j)%4, (c+j)%4

            nax, nay = x+di[na], y+dj[na]
            nbx, nby = nax+di[nb], nay+dj[nb]
            ncx, ncy = nbx+di[nc], nby+dj[nc]

            if ncx < 0 or ncx >= N or ncy < 0 or ncy >= M:
                continue

            if nbx < 0 or nbx >= N or nby < 0 or nby >= M:
                continue

            if nax < 0 or nax >= N or nay < 0 or nay >= M:
                continue

            temp += (papers[nax][nay] + papers[nbx][nby] + papers[ncx][ncy])
        
            max_num = max(temp, max_num)

    cross_score = [0, 0, 0, 0, papers[x][y]]
    cnt = 0
    for i in range(4):
        nx = x + di[i]
        ny = y + dj[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            cnt += 1
            continue
        
        cross_score[i] = papers[nx][ny]

    cross_sum = sum(cross_score)
    if cnt == 1:
        max_num = max(cross_sum, max_num)
    elif cnt == 0:
        for i in range(4):
            new_sum = cross_sum - cross_score[i]
            max_num = max(max_num, new_sum)

    return max_num


result = 0
for i in range(N):
    for j in range(M):
        new_sum = find(i, j)
        result = max(new_sum, result)

print(result)