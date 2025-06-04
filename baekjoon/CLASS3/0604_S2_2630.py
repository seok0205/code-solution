'''
S2 2630 색종이 만들기

전체 종이가 모두 같은 색을 칠해져 있지 않으면 가로, 세로 중간 부분을 잘라서 나눔.
N/2 x N/2 색종이로 나눔. 그래도 전체 종이가 같은 색이 아니면 이 과정 반복.
끝까지 반복했을 때, 하얀색, 파란색 각각 종이 개수 구하는 문제.

첫째줄은 종이 한 변의 길이 N(2, 4, 8, 16, 32, 64, 128)
둘째줄부터 종이의 윗줄부터 마지막줄까지 주어짐.
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1, 숫자 사이에 공백 존재

첫 줄에는 잘라진 하얀색 색종이의 개수 출력,
둘째 줄에는 파란색 색종이의 개수 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')


def cut_paper(x, y, n):     # 첫 좌표와 종이 길이
    global blue, white

    color = area[x][y]                  # 분면의 첫 칸의 색을 기준
    for i in range(x, x + n):           # 분면마다 색이 모두 같은지 확인
        for j in range(y, y + n):
            if color != area[i][j]:     # 만약 다르면 바로 자르기 실행
                new_n = n // 2              # 반으로 잘라야함
                cut_paper(x, y, new_n)      # 4분면 모두 재귀로 또 다시 확인
                cut_paper(x, y + new_n, new_n)
                cut_paper(x + new_n, y, new_n)
                cut_paper(x + new_n, y + new_n, new_n)
                return                  # 만약 자르기 시작하면 종이의 수를 확인할 수 없음.
    if color == 0:          # 위에서 같은 색인것을 확인했으면 각 색종이 갯수를 증가시킴
        white += 1
    else:
        blue += 1


input = sys.stdin.readline
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

cut_paper(0, 0, N)

print(white)
print(blue)