'''
D4 7465 창용 마을 무리의 개수

창용 마을에는 N명의 사람이 삼
편의상 1번부터 N번 사람까지 번호가 붙여져 있다고 가정
서로 알수도 있고, 아닐수도 있음

서로 아는 관계거나 몇 사람 거쳐 알 수 있는 관계면, 이런 사람들 다묶어서 하나의 무리로 침
창용 마을에 몇 개의 무리가 존재하는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_set(n):                            # union에 필요한 부모 노드 표시 리스트와 랭크 리스트 생성 함수
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks


def find_set(x):                            # 해당 x의 대표자 찾기
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    ref_x = find_set(x)             # 각각 x, y의 대표자 찾기
    ref_y = find_set(y)
    
    if ref_x == ref_y:              # 대표자 같으면 이미 같은 집합이란 뜻
        return
    
    if ranks[ref_x] < ranks[ref_y]:     # 랭크의 크기에 따라 합쳐지는 곳이 다름 큰쪽에 다른 쪽이 먹히는 형식
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:                               # 랭크값 같으면 그냥 한쪽에 합치고 먹은 쪽의 랭크값 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = [i for i in range(N+1)]
    parents, ranks = make_set(N)
    team = 0
    
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
        
    for i in range(N+1):                    # 집합의 개수 찾기(대표자 갯수 찾기)
        if number[i] == parents[i]:
            team += 1
            
    print(f'#{tc} {team-1}')