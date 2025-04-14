'''
S5 17290 Crazy_aRcade_Good

크레이지 아케이드를 하면서 폭탄을 피하려고 함. 게임하는 곳은 10x10 크기의 배열로 나타내기 가능.
폭탄이 있는곳은 o, 없는 칸은 x로 나타냄. 폭탄이 커질 때, 폭탄과 같은 행, 열에 있다면 물방울에 갇힘.

위치와 게임판이 주어질 때, 물방울에 갇히지 않기 위해 움직여야할 최소 이동 횟수 구하는 문제.
한 번에 한칸, 가로 혹은 세로로 이동가능. 폭탄 위를 지나갈수 있고, 움직이지 않아도 된다면 0 출력

물방울에 갇히지 않는 경우만 입력으로 주어짐
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

r, c = map(int, input().split())        # 처음 위치
arcade = [list(input()) for _ in range(10)]     # 맵

x = [True] * 10     # 이행과 열이 폭탄에 영향이 있는가
y = [True] * 10

for i in range(10):
    for j in range(10):
        if arcade[i][j] == 'o':
            x[i] = False        # 폭탄이 같은 열이나 행이 있다면 그 행과 열은 안전하지 않음
            y[j] = False     

result = float('inf')   # 최솟값 구해야하므로 높은 값 기본 설정. 무조건 안전한 곳만 주어진다고 했기에, 다른 조건 필요 X.

for a in range(10):
    if x[a]:    # 안전한 행이면
        for b in range(10):
            if y[b]:        # 안전한 열이라면
                num = abs(a-r+1) + abs(b-c+1)       # 겹치는 좌표와 현재 위치 좌표 거리 계산. 가로 세로 한칸씩 이동 가능이라 사각형 변 길이 구하면 알맞음
                result = min(num, result)           # 최솟값 비교
              
print(result)