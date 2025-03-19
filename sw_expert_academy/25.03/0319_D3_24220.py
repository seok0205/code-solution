'''
D3 24220 경로의 수

방향성 그래프가 존재
방향성 그래프와 출발, 도착 정점이 주어지면, 경로에 포함된 정점을 한 번만 방문해서
이동 가능한 경로가 몇 개인지 찾는 문제

- 모든 정점을 지날 필요 X
- 사이클이 존재할 수 있음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def dfs(s, e):      # dfs식 재귀함수
    global result
    
    if s == e:      # 목표점에 도달하면 결과 1 증가
        result += 1
        return
    
    for node in edge[s]:
        if visit[node] == 0:        # 방문안한곳만 가야함
            visit[node] = 1         # 이곳 지날 때
            dfs(node, e)            # 다음 경로 정하러 가기
            visit[node] = 0         # 0으로 만들어줘야 이곳을 지나는 다른 경우의 수도 지나갈 수 있음

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    info = list(map(int, input().split()))
    edge = [[] for _ in range(N+1)]
    start, end = map(int, input().split())
    result = 0
    
    for i in range(E):                              # 간선 세팅
        edge[info[i*2]].append(info[i*2+1])
    
    visit = [0] * (N+1)
    visit[start] = 1
    dfs(start, end)
    
    print(f'#{tc} {result}')