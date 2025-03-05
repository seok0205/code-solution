'''
D3 16720 노드의 합

완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장, 리프 노드를 제외한 노드에는
자식 노드에 저장된 값의 합이 들어있음

N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되고,
같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작

완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없음

리프노드의 번호, 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드에 저장된 값을 출력
'''


def post_order(T):      # 후위 연산하면서 부모노드의 합을 채워가는 함수
    if T <= N:
        post_order(T*2)
        post_order(T*2+1)
        if T*2 <= N and T*2+1 <= N:     # 완전 이진 트리라 둘다 있거나, 왼쪽 자식 노드만 있거나
            node[T] = node[T*2] + node[T*2+1]
        elif T*2 <= N:
            node[T] = node[T*2]
            
    

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    
    node = [0] * (N+1)      # 노드 번호별 저장된 값 리스트
    
    for _ in range(M):
        a, b = map(int, input().split())
        
        node[a] = b
        
    post_order(1)
    
    print(f'#{tc} {node[L]}')