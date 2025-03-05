'''
D3 16719 이진 힙

이진 최소힙은 다음 특징을 가짐
1. 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드 추가
2. 부모 노드의 값 < 자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꿈
3. 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가함

주어진 입력 순서대로 이진 최소힙에 저장 후, 마지막 노드의 조상 노드에 저장된 정수 합을 알아내는 문제
'''


def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p and heap[p] > heap[c]: # 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    heap = [0] * (N+1)
    last = 0
    result = 0
    
    for i in nums:
        # 노드 추가 / 부모<자식 조건 안맞으면 부모와 맞바꿈
        enq(i)
        
    while N > 0:        # 조상 노드 계산.
        N //= 2         # 이진 트리의 한 노드의 부모 노드는 번호를 차례대로 생각했을때, N//2번이다.
        result += heap[N]
        
    print(f'#{tc} {result}')