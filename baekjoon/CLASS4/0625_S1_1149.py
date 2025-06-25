'''
S1 1149 RGB거리

RGB거리에는 집이 N개 있음. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함. 각각 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어질 때, 집을 칠하는 비용의 최솟값을 구하는 문제.
1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
3. i(2 <= i <= N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

입력:
N - 집의 수
N개의 줄에 번호 순대로 빨강 초록 파랑(칠하는 비용) 주어짐.

출력:
모든 집을 칠하는 비용의 최솟값
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
rgb = [0] * N       # 집마다 색을 칠하면서 비용을 저장할 리스트

for i in range(N):
    r, g, b = map(int, input().split())
    rgb[i] = [r, g, b]      # i번째 집의 비용.

for i in range(1, N):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]       # 이전 번호의 집과 같은 색은 못칠하기 때문에, 둘중 하나 선택해야 함.
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]       # 어차피 최솟값 구하는 게 목표기 때문에 r이 이전 색이면 r에 g, b중 작은 값을 더해줘야 함.
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

result = min(rgb[N-1][0], rgb[N-1][1], rgb[N-1][2])         # 최솟값이 답

print(result)