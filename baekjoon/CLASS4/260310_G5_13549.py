'''
G5 13549 숨바꼭질 3

문제 설명:
숨바꼭질 중이다. 나는 현재 점 N에 있고, 찾으려는 사람은 점 K에 있다. 난 걷거나 순간이동을 할 수 있다.
만약 내 위치가 X일 때 걷는다면 1초 후에 X-1 혹은 X+1로 이동 가능하다.
순간이동하는 경우, 0초후에 2*X의 위치로 이동한다.
나와 찾으려는 사람의 위치가 주어질 때, 내가 가장 빨리 사람을 찾을 수 있는 시간이 몇 초 후인지 구하는 문제.

입력:
첫째 줄 - N, K (정수고 각각 0보다 크거나 같고, 100,000보다 작거나 같다.)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque

N, K = map(int, input().split())
area = [float('inf')] * 100001

def solution():
    q = deque([N])
    area[N] = 0

    while q:
        now = q.popleft()

        if now == K:
            output(str(area[K]))
            return

        nx = now * 2
        if 0 <= nx < 100001 and area[nx] == float('inf'):
            area[nx] = area[now]
            q.appendleft(nx)
        
        for nx in [now-1, now+1]:
            if 0 <= nx < 100001 and area[nx] == float('inf'):
                area[nx] = area[now] + 1
                q.append(nx)

solution()