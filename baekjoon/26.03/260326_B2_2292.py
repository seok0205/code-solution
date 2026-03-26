'''
B2 2292 벌집 복습

문제 설명:
육각형으로 이루어진 벌집.
중앙의 방 1부터 시작해 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매김.
숫자 N이 주어질 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는 지 (시작, 끝 포함)를 계산하는 문제.
예로, 13은 3개, 58까지는 5개 지남.

입력:
첫째 줄 - N (1 <= N <= 1000000000)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
room_num = 1
temp = 1

while N > room_num:
    room_num += (6*temp)
    temp += 1

print(temp)