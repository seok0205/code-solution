'''
G5 14719 빗물

문제 설명:
2차원 세계에 블록이 쌓여있다.
비가오면 블록 사이에 빗물이 고임.

비는 충분히 많이옴. 고이는 빗물의 총량은?

입력:
첫번째 줄에는 2차원 세계의 세로 길이 H와 가로길이 W가 주어짐 (1 <= H, W <= 500)
두번째 줄 - 블록이 쌓인 높이를 의미하는 0이상 H이하 정수가 2차원 세계의 맨 왼쪽 위치부터 차례로 W개 주어짐.
따라서 블록 내부의 빈 공간이 생길 수 없음.
바닥은 항상 막혀있다고 가정.

출력:
2차원 세계에서는 한칸이 용량 1임. 고이는 빗물의 총량은?
안 고이면 0 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

H, W = map(int, input().split())
world = list(map(int, input().split()))
new_world = [[0] * W for _ in range(H)]
result = H * W - sum(world)

for j in range(W):
    for i in range(H):
        if world[j] - 1 < i:
            continue

        new_world[i][j] = 1

no_wall = 0
for i in range(H):
    temp = 0
    for j in range(W):
        if new_world[i][j]:
            break
        
        temp += 1
    else:
        no_wall += 1
    
    result -= temp

for i in range(H):
    temp = 0
    for j in range(W-1, -1, -1):
        if new_world[i][j]:
            break
        
        temp += 1
    
    result -= temp

result += (no_wall * W)
print(result)