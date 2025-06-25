'''
S2 11725 트리의 부모 찾기

루트 없는 트리가 주어짐. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 문제

입력:
첫째 줄 : N(노드 개수)
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어짐.

출력:
N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def dfs(node):      # dfs로 부모 노드 찾기
    stack = [node]  # 시작 노드
    while stack:        # 스택이 빌 때까지 실행
        x = stack.pop()
        for i in edge[x]:           # 만약 해당 노드와 연결되어 있고
            if visit[i] == 0:       # 방문 안했으면
                visit[i] = x        # 부모노드로 정하고 저장.
                stack.append(i)     # 스택에 넣기


N = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(N-1):                    # edge에 정점 연결 정보 저장
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

visit = [0] * (N+1)     # 방문 리스트(부모 노드도 저장하는 곳)

dfs(1)

for i in range(2, N+1):
    print(visit[i])