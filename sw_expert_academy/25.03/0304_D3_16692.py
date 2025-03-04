'''
D3 16692 이진탐색

1부터  N까지의 자연수를 이진 탐색 트리에 저장하려 함
어떤 경우에도 저장된 값이 왼쪽 서브 트리의 루트 -> 현재 노드 -> 오른쪽 서브 트리의 루트인 규칙 만족

완전 이진 트리의 노드 번호는 루트를 1번, 아래로 내려가면서 왼쪽에서 오른쪽으로 증가
N이 주어질 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값, N//2 번 노드에 저장된 값 구하는 문제
'''


def find_node(node):
    global idx
    if node <= N:       # N이하여야함. N이 총 갯수이기 때문
        find_node(node*2)       # 왼쪽 서브트리
        visit[node] = idx       # 현재 노드
        find_node(node*2+1)     # 오른쪽 서브트리
    else:               # 끝에 막히면 idx가 증가하기 시작 가장 깊은 곳에서 숫자 증가하게 만듦
        idx += 1
        
    
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    visit = [0] * (N+1)     # 방문 후 값 저장할 리스트
    idx = 0
    find_node(1)    # 중위 순회 찾기

    result_1 = visit[1]         # 정답 조건 : 첫번째 노드의 값, N//2번째 노드의 값
    result_2 = visit[N//2]
    print(f'#{tc} {result_1} {result_2}')