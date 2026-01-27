'''
S1 1389 케빈 베이컨의 6단계 법칙

문제 설명:
모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결 가능
케빈 베이컨 수가 가장 작은 사람 찾으려고 함.
케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합.

1과 3, 1과 4, 2와 3, 3과 4, 4와 5가 친구인 경우
1은 2까지 2단계, 3까지 1단계, 4까지 1단계, 5까지 2단계 만에 알 수 있음.
따라서 1은 케빈 베이컨 수가 8.
이렇게 계산하면 케빈 베이컨수 가장 작은사람은 3이랑 4임.
친구 관계가 입력으로 주어질 때, 가장 작은 사람 구하는 문제.

입력:
첫줄 - N (2~100) M (1~5000)
둘째 줄부터 M개의 줄에 친구 관계.
(a, b) - a와 b가 친구라는 뜻. 양방향, A, B 같은 경우 없음.
중복으로 들어올 수도 있음. 친구 없는사람은 없음.
모든 사람들은 연결되어있음. 1부터 N번. 두 사람이 같은 번호 불가능.

출력:
가장 작은 사람 출력. 여러 명이면 가장 작은 사람 출력(번호)
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().strip().split())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().strip().split())
    edge[s].append(e)
    edge[e].append(s)

min_bacon = float('inf')

for i in range(1, N+1):
    bacon = 0
    q = deque([i])
    visit = [0] * (N+1)
    visit[i] = 1

    while q:
        x = q.popleft()
        for k in edge[x]:
            if i == k:
                continue

            if visit[k]:
                continue
            
            q.append(k)
            visit[k] = visit[x] + 1
            bacon += visit[k]
    
    if min_bacon > bacon:
        min_bacon = bacon
        result = i

output(str(result))