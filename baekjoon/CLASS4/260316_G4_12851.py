'''
G4 12851 숨바꼭질 2

문제 설명:
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동 가능.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성.

입력:
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수.

출력:
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력.
둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque

N, K = map(int, input().split())

visit = [-1] * 100001
q = deque([N])
visit[N] = 0

time = 0
cnt = 0

while q:
    now = q.popleft()
    
    if now == K:
        time = visit[now]
        cnt += 1
        continue

    for nx in (now + 1, now - 1, 2 * now):
        if nx < 0 or nx > 100000:
            continue

        if visit[nx] == -1 or visit[nx] == visit[now] + 1:
            visit[nx] = visit[now] + 1
            q.append(nx)

output(str(time) + '\n' + str(cnt))