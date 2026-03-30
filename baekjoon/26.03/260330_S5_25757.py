'''
S5 25757 임스와 함께하는 미니게임

문제 설명:
미니게임 같이할 찾는 중.
윷놀이 Y, 같은 그림찾기 F, 원카드 O가 있음.
각각 2, 3, 4명이서 플레이하는 게임.
인원수 부족 시 시작 불가.
사람들이 플레이하기를 신청한 횟수 N, 임스가 플레이할 게임 종류가 주어질 때, 최대 몇 번이나 함께 플레이할 수 있는지 구하는 문제.
여러번 플레이하고자 하는 사람이 있으나, 한번 같이하면 다시 플레이 안함.
동명이인 없음.

입력:
신청한 횟수 N - (1 <= N <= 100000), 게임 종류
두번째 줄부터 N개의 줄에 플레이하고자 하는 사람 이름(1 <= 문자열 길이 <= 20)
사람들 이름은 숫자 혹은 영문 대소문자로 구성.

출력:
최대로 몇번이나 플레이할 수 있는지 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

data = input().strip().split()
N = int(data[0])
game = data[1]
members = set()

if game == 'Y':
    game_mem = 2
elif game == 'F':
    game_mem = 3
else:
    game_mem = 4

for _ in range(N):
    name = input().strip()
    members.add(name)

num = len(members)
result = num // (game_mem-1)
print(result)