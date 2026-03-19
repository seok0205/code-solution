'''
G3 1865 웜홀

문제 설명:
N개의 지점이 있고, N개의 지점 사이에 M개의 도로와 W개의 웜홀이 있음.
도로는 방향이 없지만 웜홀은 방향이 있음.
웜홀은 시작 위치에서 도착위치로 가는 하나의 경로, 특이하게 도착을 하게 되면 시작 했을때 보다 시간이 뒤로가짐.

한 지점에서 출발해서 시간여행을 하기 시작해 다시 출발을 했던 위치로 다시 돌아올 때, 출발 했을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해짐.
가능 불가능 여부 구하는 문제.

입력:
첫째 줄 - TC 개수 (1 <= TC <= 5)
각 TC의 첫 줄 - N(1 <= N <= 500), M(1 <= M <= 2500), W(1 <= W <= 200)
두번 째 줄부터 M개의 줄에 도로 정보, (S, E, T)
M개의 줄이 끝나면 웜홀의 정보, (S, E, T)
두 T의 차이는 걸리는 시간, 줄어드는 시간.

출력:
만약 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 아니면 NO 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write


def func():
    N, M, W = map(int, input().split())
    edge = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        edge.append((s, e, -t))

    visit = [0] * (N+1)

    for i in range(N):
        for s, e, t in edge:
            if visit[e] > visit[s] + t:
                visit[e] = visit[s] + t

                if i == N-1:
                    return True
    
    return False


TC = int(input())

for _ in range(TC):
    if func():
        output('YES' + '\n')
    else:
        output('NO' + '\n')