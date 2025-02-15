'''
D5 1248 공통조상

이진 트리에서 임의의 두 정점의 가장 가까운 공통 조상을 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 문제
루트 정점은 항상 1번

입력:
테스트케이스
정점 개수 V, 간선 개수 E, 공통 조상 찾을 두개의 번호
E개 간선 나열(부모 자식 순서)
'''


def dfs_find_same_root(s, edge_lst, v):     # DFS 활용 함수
    visited = [0] * (v+1)
    stack = []
    stack.append(s)
    num = 0         # 노드를 방문한 순서를 담을 변수
    
    while True:
        num += 1        # 노드 방문 순서 1 누적
        if visited[s] == 0:     # 노드 첫 방문 시의
            visited[s] += num       # 순서 지정

        for w in edge_lst[s]:       # 해당 노드과 연결된 노드
            if visited[w] == 0:     # 첫 방문이면
                stack.append(w)     # 스택에 w 추가
                s = w               # 다음 방문 노드로 지정
                break       # while문의 처음으로 돌아가 다음 방문 노드를 방문
        else:       # 만약 연결된 노드를 다 방문 했다면
            if stack:       # 스택에 저장된 노드로 돌아감(이전 방문했던 노드)
                s = stack.pop()
            else:       # 스택이 비어있어 가장 처음 방문했던 노드에 위치해 있다면
                break   # while문 종료
    return visited      # 방문 기록 남은 리스트 반환
                

T = int(input())

for tc in range(1, T+1):
    V, E, node1, node2 = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    
    edge = [[] for _ in range(V+1)]     # 트리의 크기 구할 때 활용할 각 노드와 연결된 자식노드 정보
    reverse_edge = [[] for _ in range(V+1)]     # 공통 조상 노드 구할 때 활용할 각 노드와 연결된 부모노드 정보
    for i in range(E):
        a = lst[i*2]
        b = lst[i*2+1]
        reverse_edge[b].append(a)   # 부모노드는 역방향
        edge[a].append(b)   # 자식노드는 정방향 정보 저장

    lst_one = dfs_find_same_root(node1, reverse_edge, V)    # 첫번째 노드가 거슬러 올라갈 때 방문하는 순서 정보 리스트
    lst_two = dfs_find_same_root(node2, reverse_edge, V)    # 두번째 노드가 거슬러 올라갈 때 방문하는 순서 정보 리스트
    
    compare = []        # 공통 조상노드 구할 때 사용할 리스트
    for idx in range(V+1):                                      # 방문 순서를 담은 반환된 리스트를 순회하면서
        if lst_one[idx] and lst_two[idx]:                       # 만약 두 리스트의 같은 인덱스에 값이 존재한다면, 공통된 조상노드 가지고 있다는 것
            compare.append((idx, lst_one[idx] + lst_two[idx]))  # compare리스트에 해당 노드번호(idx)와 방문순서의 합을 구함
                                                                # 합을 구하는 이유는 방문 순서의 합이 가장 작다면 겹치는 조상노드 중 가장 먼저 방문했다는 의미
    root_node = compare[0][0]   # root_node : 공통된 조상노드, num : 방문순서 최솟값(compare에 먼저 담긴 값들로 초기화)
    num = compare[0][1]
    for i, j in compare:        # compare에 담긴 tuple의 idx, 방문순서의 합을 각각 i, j로 지정하고 순회
        if j < num:             # 만약 num보다 j가 작으면 더 일찍 방문한 조상노드라는 의미
            num = j             # num을 방문순서 합으로
            root_node = i       # root_node(조상노드)를 idx로 교체

    tree_size = 0       # tree_size : 조상노드가 정점인 서브트리의 크기
    lst_three = dfs_find_same_root(root_node, edge, V)      # root_node가 정점인 트리의 방문 정보 리스트 반환
    for i in lst_three:
        if i:                   # 방문 정보 리스트의 값이 0이 아니면 서브트리에 해당된다는 것(방문했기 때문에)
            tree_size += 1      # 트리 크기 1증가
    
    print(f'#{tc} {root_node} {tree_size}')     # 결과값 출력