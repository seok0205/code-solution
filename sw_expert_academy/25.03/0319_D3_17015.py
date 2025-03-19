'''
D3 17015 그룹 나누기

수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출

한 조에 인원의 제한을 두지 않았음. 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우
모두 같은 조가 됨

예로 1-2, 1-3이 같은 조가 되고 싶다고 하면, 1-2-3이 같은 조가 됨
번호 적지 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성함

1번부터 N번까지 출석 번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_set(n):                        # 그룹 합에 필요한 n+1 길이의 부모노드, 랭크 표현 리스트 생성
    member = [i for i in range(n+1)]
    rank = [0] * (n + 1)
    return member, rank


def find_set(x):                            # 해당 x노드의 루트 노드 찾기(대표자)
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):                    # x, y 이 속한 그룹들 합치기
    ref_x = find_set(x)             # x 대표자 찾기
    ref_y = find_set(y)             # y 대표자 찾기
    
    if ref_x == ref_y:              # 대표자 같단건 이미 같은 그룹
        return
    
    if ranks[ref_x] < ranks[ref_y]:     # 랭크가 y가 속한 집합이 더 크면 y에 x 대표자가 들어감
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:                               # 같으면 그냥 한쪽에 합치고 먹은 쪽이 랭크 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    parents, ranks = make_set(N)
    
    for i in range(M):
        union(paper[i*2], paper[i*2+1])
        
    cnt = 0
    member = [i for i in range(N+1)]
    for i in range(N+1):                        # 대표자 찾으면 전체 집합 수. 부모노드 리스트와 자기 자신의 노드번호 같으면 대표자 증명.
        if member[i] == parents[i]:
            cnt += 1
        
    print(f'#{tc} {cnt-1}')