'''
D4 4408 자기 방으로 돌아가기

숙소가 복도를 따라 400개의 방이 존재
1번 맞은편 2번, 1번방 오른쪽이 3번, 3번 맞은편이 4번, 3번 오른쪽이 5번... 형태로 배열되어있음

만약 두 사람이 자기방으로 돌아가는 도중에 지나는 복도의 구간이 겹치면 동시에 못드감
이동하는 데에는 거리 상관없이 단위 시간이 걸림

각 사람들의 방 위치와 돌아가야 할 방 위치 목록이 주어질 때, 최소 몇 단위 시간만에 모든 학생이 이동할 수 있는지 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cur_room = [0] * 401
    
    for _ in range(N):
        a, b = map(int, input().split())
        
        cur_room[a] = (b)

    for i in range(len(cur_room)):
        if cur_room[i]:
            location = i
            