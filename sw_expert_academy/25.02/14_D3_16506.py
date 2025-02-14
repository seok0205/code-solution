'''
D3 16506 그래프 경로

V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 문제
두 개의 노드에 대해 경로에 있으면 1, 없으면 0 출력

노드번호는 1번부터 존재, V개의 노드 중에는 간선으로 연결되지 않는 경우도 있을 수 있음

입력:
테스트 케이스
V, E
E개의 줄에 걸쳐 출발 도착노드로 간선 정보 주어짐
경로의 존재를 확인할 출발노드 S, 도착노드 G 주어짐
'''


def find_node(s, g):
    visited = [0] * (g + 1)     # 방문한 노드 0: 방문 안함, 1: 방문 함
    stack = []

    while True:
        if visited[s] == 0:     # 첫 시작 노드는 visited를 1로 만들고 시작
            visited[s] = 1
        for k in node_lst[s]:       # 만약 s에서 갈 수 있는 노드가
            if visited[k] == 0:     # 방문 안했으면
                stack.append(s)     # 스택에 추가
                s = k               # 현재 노드가 됨
                break
        else:                       # 만약 바뀔 노드가 없으면 갈 곳 이 없다는 뜻
            if stack:               # 돌아감
                s = stack.pop()     # 스택에서 팝
            else:                   # 더 돌아갈 곳이 없다면 while문 끝
                break

    return visited


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_lst = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        node_lst[a].append(b)
    S, G = map(int, input().split())

    visited_lst = find_node(S, V)

    if visited_lst[G] == 1:     # 만약 visited의 G번째 노드가 1이면 방문할 수 있다는 뜻
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
