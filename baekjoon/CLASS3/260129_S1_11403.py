'''
S1 11403 경로 찾기

문제 설명:
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i,j)에 대해서 i에서 j로 가는 길이가
양수인 경로가 있는지 없는지 구하는 프로그램 작성

입력:
첫 줄 - N (1~100)
둘째 줄 부터 N개의 줄 - 그래프의 인접 행렬 주어짐.
i번째 줄의 j번째 숫자가 1인 경우, i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻.
i번째 줄의 i번째 숫자는 항상 0.

출력:
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력.
정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 함.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
graph = []

for _ in range(N):
    row = list(map(int, input().strip().split()))
    graph.append(row)

for s in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] or (graph[i][s] and graph[s][j]):
                graph[i][j] = 1

for row in graph:
    output(' '.join(map(str, row)) + '\n')