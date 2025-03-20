'''
D3 17030 최소 이동 거리

A도시에 E개의 일방통행 도로 구간이 있음. 각 구간이 만나는 연결지점에는 0부터 N번까지 번호 존재
구간 시작 끝의 연결 지점 번호, 구간 길이가 주어질 때, 0번 지점에서 N번 지점까지 이동하는데
걸리는 최소한의 거리가 얼마인지 출력하는 문제

모든 연결지점을 거쳐가야 하는 건 아님
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

import heapq


def dijkstra(s):
    hq = [(0, s)]
    visit = [INF] * (N+1)       # 해당 노드 까지 가기까지의 최소 거리 담을 리스트
    visit[s] = 0                # 시작 노드는 도달 거리 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        
        if visit[node] < dist:      # 방문했으면 넘어감(inf가 기본값이라서 방문 안했으면 무조건 visit[node]가 더 크기때문), 그리고 방문 했어도 이미 최솟값의 조건 가진 값이 visit[node]에 자리하고 있으면 다음으로 넘어감
            continue
        
        for next_info in edge[node]:        # 간선 정보를 불러옴
            next_dist = next_info[1]        # 거리
            next_node = next_info[0]        # 다음 노드
            
            new_dist = dist + next_dist     # 지금까지 거리와 다음 노드까지 거리 합친 것이 새로운 거리
            
            if visit[next_node] <= new_dist:        # 만약 다음 노드까지의 누적 거리보다 new_dist가 더 크면 이미 최솟값 조건 박탈. 다음 경로 탐색 
                continue
            
            visit[next_node] = new_dist             # 새로운 값으로 대체
            heapq.heappush(hq, (new_dist, next_node))       # 다음 경로 봐야하므로 힙푸시
            
    return visit


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    edge = [[] for _ in range(N+1)]
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge[s].append((e, w))

    INF = float("inf")
    
    result = dijkstra(0)
    
    print(f'#{tc} {result[N]}')