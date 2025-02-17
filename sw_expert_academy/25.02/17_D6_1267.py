'''
D6 1267 작업순서

V개의 작업이 있는데, 몇몇 선행 작업이 끝나야 시작할 수 있음
작업들과 선행관계가 주어지면 작업 순서를 출력하는 문제
'''

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    visited = [1] * (V+1)       # 수행안하면 1, 수행 하면 0으로 저장할 방문 목록
    edge_lst = [[] for _ in range(V+1)]     # 이전 노드. 즉, 각 노드실행에 필요한 선행노드가 담겨있음
    for i in range(E):
        a = edge[i*2]
        b = edge[i*2+1]
        
        edge_lst[b].append(a)
        
    result = list()     # 결과 리스트
    cnt = V
    
    while cnt:      # 모두 수행해야함
        for i in range(1, len(edge_lst)):       # 1번부터 마지막 노드까지 반복
            if visited[i]:          # 현재 노드 수행안했다면
                for j in edge_lst[i]:       # 선행노드를 확인
                    if visited[j]:          # 선행노드 안했다면
                        break               # 반복 중단.
                else:                       # 선행노드가 모두 수행되었으면
                    visited[i] = 0          # 방문했다고 기록 남김
                    result.append(i)        # 순서대로 결과에 추가
                    cnt -= 1                # 하나 방문했으므로 남은 개수 -1
    
    print(f'#{tc} {" ".join(list(map(str, result)))}')