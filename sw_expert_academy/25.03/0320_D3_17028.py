'''
D3 17028 최소 신장 트리

그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이
최소가 되도록 만든 경우를 최소신장트리라고 함

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보 주어질 때,
이 그래프의 최소 신장 트리를 구성하는 간선의 가중치를 모두 더해 출력하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

import heapq


def prim(s):                    # 프림 알고리즘 사용
    hq = [(0, s)]
    MST = [0] * (V+1)           # 방문한 노드 리스트
    min_weight = 0              # 최소 합
    
    while hq:
        weight, node = heapq.heappop(hq)        # 가중치, 노드 디큐
        
        if MST[node]:               # 방문했으면 다음 노드
            continue
        
        MST[node] = 1               # 방문 표시
        min_weight += weight        # 현재 간선의 가중치 더해줌
        
        for next_node in range(V+1):        # 노드와 연결된 다음 간선들 찾아봄
            if graph[node][next_node] == 0:         # 가중치 없으면 다음 노드 찾음(연결된 간선없다는 뜻)
                continue
            
            if MST[next_node]:              # 이미 방문한 노드도 넘김
                continue
            
            heapq.heappush(hq, (graph[node][next_node], next_node))     # 방문 안했고, 연결된 간선 존재하면 인큐
        
    return min_weight
    


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    
    for _ in range(E):
        a, b, c = map(int, input().split())     # 해당 노드 a, b를 연결하는 간선의 가중치 c
        graph[a][b] = c                         # 양방향으로 넣어줌
        graph[b][a] = c
        
    result = prim(1)
    print(f'#{tc} {result}')