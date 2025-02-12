'''
D1 20396 돌 뒤집기 게임 1

동전처럼 생긴 돌의 양면은 흰색 검은색.
뒤집기는 i번째 j개의 돌을 i번째 돌의 색으로 바꿔놓음

입력:
T - 게임 개수
N, M = N은 돌, M은 뒤집는 횟수
N개의 돌의 배열
i, j
'''

import sys
sys.stdin = open('seok.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    iandj = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(iandj)):     # i, j 주어진 케이스 마다
        for j in range(iandj[i][1]):    # j는 바꿔야할 횟수
            x = iandj[i][0] - 1     # i에 해당되는 돌을 x
            if 0 < x+j < N:         # 바꾸려는 위치가 배열 안이면
                stone[x+j] = stone[x]       # i에 해당된 돌과 바꾸려는 돌의 색을 같게 만듬

    print(f"#{tc} {' '.join(map(str, stone))}")
