'''
D4 3124 최소 스패닝 트리

그래프가 주어질 때, 그 그래프의 최소 스패닝 트리를 구하라
최소 스패닝 트리는, 주어진 그래프의 모든 저점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리 말함
입력으로 주어지는 그래프는 하나의 연결 그래프임이 보장
'''

import sys
sys.stdin = open('tc.txt', 'r')

import heapq


def prim(s):
    q = [(0, s)]
    visit = [0] * (V+1)
    min_w = 0
    
    while q:
        w, n = heapq.heappop(q)
        
        if visit[n]:
            continue
        
        visit[n] = 1
        min_w += w
        
        for next_w, next_n in graph[n]:
            if visit[next_n]:
                continue
            
            heapq.heappush(q, (next_w, next_n))
    
    return min_w


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
        
    result = prim(1)
    print(f'#{tc} {result}')