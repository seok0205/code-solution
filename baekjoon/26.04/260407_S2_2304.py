'''
S2 2304 창고 다각형

문제 설명:
N개의 막대 기둥이 일렬로 세워져 있음.
기둥들의 폭은 모두 1m이며 높이는 다를 수 있음.
이 기둥들을 이용해 양철로 된 창고를 제작하려 함.
창고에는 모든 기둥이 들어감.
창고의 지붕을 다음과 같이 만듦.

1. 지붕은 수평 부분과 수직 부분으로 구성. 모두 연결되어야 함.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 함.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 함.
4. 지붕의 가장자리는 땅에 닿아야 함.
5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분 없어야 함.

옆에서 본 모습을 창고 다각형이라고함. 창고 다각형의 면적이 제일 작은 창고를 만들기를 원함.
기둥들의 위치 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램 작성.

입력:
기둥수 정수 N. 1 이상 1,000 이하.
N개의 줄에는 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어짐.
L과 H는 둘 다 1 이상 1,000이하.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
pillars = []
right = 0

for _ in range(N):
    l, h = map(int, input().split())
    pillars.append((l, h))
    if right < l:
        right = l

garage = [0] * (right + 1)

for l, h in pillars:
    garage[l] = h

max_height = 0
max_location = 0
for i in range(len(garage)):
    if garage[i] > max_height:
        max_height = garage[i]
        max_location = i

total = 0

now_max = 0
for i in range(max_location + 1):
    now_max = max(now_max, garage[i])
    total += now_max

now_max = 0
for i in range(right, max_location, -1):
    now_max = max(now_max, garage[i])
    total += now_max

print(total)