'''
S2 18111 마인크래프트

문제설명:
마인크래프트의 블록은 1x1x1크기.
마인크래프트에서 집을지으려고 함. 땅 고르기 작업해야함.
세로 N, 가로 M이 집터를 골랐고, 맨 왼쪽 위의 좌표는 0,0임.
집터 내의 땅 높이를 일정하게 바꿔야함.
1. 좌표 i,j의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록하나를 꺼내 좌표 i,j의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초, 2번 작업은 1초 걸림. 최대한 빨리 끝내야 함.
최소 시간, 땅의 높이를 출력

단, 집터 아래 동글 등 빈공간은 없고, 집터 바깥에서 블록은 못 가져옴. 또한, 작업 시작 시
인벤에는 B개의 블록이 있음. 땅의 높이는 256은 초과 못하고, 음수는 불가능.

입력:
첫 줄 - N, M, B (1~, ~500, 0~6.4x10**7)
둘째 줄부터 N개의 줄에 M개의 정수로 땅 높이 주어짐.
i+2 번째 줄의 j+1 번째 수는 좌표 i,j의 땅높이를 나타냄.
땅높이는 0~255

출력:
땅을 고르는데 걸리는 시간과 땅의 높이 출력. 답이 여러개면 그중에서 땅의 높이가 가장 높은것 출력
'''

import sys
from collections import Counter
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M, B = map(int, input().strip().split())
lands = []
result = float('inf')
height = 0

for _ in range(N):
    land = list(map(int, input().strip().split()))
    lands.extend(land)
count = Counter(lands)

for i in range(257):
    remove_block = 0
    stack_block = 0

    for h, cnt in count.items():
        if h < i:
            stack_block += (i - h) * cnt
        else:
            remove_block += (h - i) * cnt
    
    if B + remove_block < stack_block:
        continue

    temp = (remove_block * 2) + stack_block
    if result >= temp:
        result = temp
        height = i

output(str(result) + ' ' + str(height))