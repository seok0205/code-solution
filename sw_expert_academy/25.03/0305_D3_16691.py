'''
D3 16691 subtree

트리의 일부를 서브트리라 함
노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 문제

부모, 자식 노드 번호 사이에 특별한 규칙 없음
부모가 없는 노드가 전체의 루트 노드가 됨

부모 노드를 인덱스로 했을 때,
자식 노드 값이 0인 경우는 노드가 자식이 없다는 뜻
'''


def pre_order(T):       # 전위 순회 함수
    global cnt
    
    if T:
        cnt += 1
        pre_order(left_lst[T])
        pre_order(right_lst[T])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    
    left_lst = [0] * (E+2)
    right_lst = [0] * (E+2)
    cnt = 0                 # 서브 트리 방문 수 = 방문을 다하면 트리 크기와 같다
    
    for i in range(E):      # 받은 입력 정보를 각각 자식 노드 리스트에 반영해줌
        x = edge[2*i]
        y = edge[2*i+1]
        if left_lst[x] == 0:
            left_lst[x] = y
        else:
            right_lst[x] = y
        
    pre_order(N)        # 전위 순회하여 cnt값 알아내기
    
    print(f'#{tc} {cnt}')