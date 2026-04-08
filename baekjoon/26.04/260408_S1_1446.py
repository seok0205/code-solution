'''
S1 1446 지름길

문제 설명:
학교에 가기 위해 차를 타고 D킬로미터 길이 고속도로 지남.
이 고속도로는 심각하게 커브가 많아 운전하기 힘듦.
어느날, 이 고속도로에 지름길이 있단 것을 알게 됨.
모든 지름길은 일방통행, 고속도로를 역주행 못함.
운전해야 하는 거리의 최솟값 구하는 문제.

입력:
첫째 줄 - 지름길의 개수 N, 고속도로 길이 D.
N은 12 이하인 양의 정수, D는 10,000보다 작거나 같은 자연수.
다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이 주어짐.
모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수.
지름길의 시작 위치는 도착 위치보다 작다.

출력:
운전해야하는 거리의 최솟값 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


N, D = map(int, input().split())
visit = [float('inf')] * (D+1)

# from collections import deque

# shortcut = dict()

# for _ in range(N):
#     s, e, dist = map(int, input().split())
#     if s in shortcut:
#         shortcut[s].append((e, dist))
#     else:
#         shortcut[s] = [(e, dist)]

# q = deque([(0, 0)])

# while q:
#     now, total = q.popleft()

#     if now in shortcut:
#         for end, dist in shortcut[now]:
#             new_dist = total + dist
#             q.append((end, new_dist))
#             visit[end] = min(visit[end], new_dist)

#     if now < D:
#         q.append((now + 1, total + 1))    
#         visit[now + 1] = min(visit[now+1], total + 1)

import heapq

route = [[] for _ in range(D+1)]

for i in range(D):
    route[i].append((i+1, 1))

for _ in range(N):
    s, e, dist = map(int, input().split())
    if e <= D:
        route[s].append((e, dist))

visit[0] = 0
hq = [(0, 0)]

while hq:
    now, total = heapq.heappop(hq)

    if total > visit[now]:
        continue

    for end, dist in route[now]:
        new_total = total + dist
        if new_total < visit[end]:
            visit[end] = new_total
            heapq.heappush(hq, (end, visit[end]))

print(visit[D])