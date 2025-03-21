'''
D4 1251 하나로

N개의 섬들을 연결하려함
반드시 두 섬을 선분으로 연결, 선분이 교차된다 하더라도 물리적으로는 연결되지 않는 것으로 가정

환경 부담 세율(E)과 각 해저터널의 길이(L)의 제곱의 곱(E * L ^ 2)만큼 지불
환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템 설계

64비트 integer 및 double로 처리안하면 overflow 발생 가능
'''

import sys
sys.stdin = open('tc.txt', 'r')

# import heapq


# def prim(tax):            # 프림 알고리즘 활용
#     hq = [(0, 0)]
#     visit = [0] * N       # 섬 방문 리스트
#     min_cost = 0          # 최소 비용
    
#     save_cost = [float("inf")] * N        # 비용 저장 리스트
#     save_cost[0] = 0
#     cnt = 0                               # 연결한 섬 개수
    
#     while hq and cnt < N:                 # 힙큐에 정보 있고, 모든 섬연결하기전까진 반복
#         cost, island = heapq.heappop(hq)

#         if visit[island]:                 # 이미 방문했다면 다음 정보
#             continue
        
#         visit[island] = 1                 # 방문하고
#         min_cost += cost                  # 최솟값에 더해주고
#         cnt += 1                          # 섬 하나 연결했다고 기록
        
#         for next_island in range(N):      # 다음 갈 수 있는 섬 탐색
#             if visit[next_island]:        # 방문한 곳은 추가 안함
#                 continue
            
#             new_cost = ((island_x[next_island] - island_x[island]) ** 2 + (island_y[next_island] - island_y[island]) ** 2) * tax

#             if new_cost < save_cost[next_island]:     # 가격이 저장된 가격보다 낮다면 교체하고, 다음 탐색할 노드로 설정
#                 save_cost[next_island] = new_cost
#                 heapq.heappush(hq, (new_cost, next_island))

#     return round(min_cost)


def find_set(x):                        # 크루스칼 알고리즘 활용
    if x == parents[x]:                 # 대표자 찾기 함수
        return x
    
    parents[x] = find_set(parents[x])   # 경로 압축
    return parents[x]


def union(x, y):                        # 유니온 함수
    ref_x = find_set(x)                 # 각각 대표자 찾아서
    ref_y = find_set(y)
    
    if ref_x == ref_y:                  # 이미 같은 집합이면 종료
        return
    
    if ref_x < ref_y:                   # 전체 하나의 대표자를 첫번째 섬으로 만들면 됨. 그래서 대표자 작은 것에 계속 포함시키다보면 결국 대표자는 첫번째 섬이됨
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())
    
    # result = prim(E)
    
    parents = [i for i in range(N)]
    result = 0
    
    edges = []              # 섬과 섬이 연결된 간선 저장
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((island_x[i] - island_x[j]) ** 2 + (island_y[i] - island_y[j]) ** 2) * E
            edges.append((i, j, cost))      # 섬의 위치와 환경부담금 저장
            
    edges.sort(key=lambda x: x[2])  # 환경부담금 적은 순서로 정렬
    
    count = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v):  # 연결 계속 하면 환경부담금 적은것부터 합치기 때문에 최솟값 구하기 가능
            union(u, v)
            result += w
            count += 1
        if count == N - 1:      # count는 합친 섬의 개수. 모두 다합치면 탈출
            break
    
    result = round(result)      # 정수 형태로 반올림
    
    print(f'#{tc} {result}')