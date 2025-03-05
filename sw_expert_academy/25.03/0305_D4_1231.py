'''
D4 1231 중위 순회

주어진 트리를 in-order(중위 순회)로 읽으면 특정 단어 알 수 있음
중위 순회 했을 때 나오는 단어를 출력
'''


def in_order(T):
    global result
    
    if T:
        in_order(left[T])       # 중위 순회 함수
        result += dic[T]        # result 변수에 해당 글자 대입
        in_order(right[T])


for tc in range(1, 11):
    N = int(input())
    
    left = [0] * (N+1)      # 왼쪽 자식노드
    right = [0] * (N+1)     # 오른쪽 자식노드
    
    dic = {}                # 해당 노드에 담긴 문자열 담을 딕셔너리
    result = ''
    
    for _ in range(N):
        info = list(map(str, input().split()))
        
        dic[int(info[0])] = info[1]     # 딕셔너리에 노드번호: 문자열 형태로 대입
        
        if info[2:]:        # 만약 받은 info에 자식 노드에 관한 정보가 있따면(자식 정보는 인덱스 2부터 등장)
            left[int(info[0])] = int(info[2])
        
        if info[3:]:        # 만약 받은 info에 자식 노드에 관한 정보가 2개 있다면(두번째 자식 노드 정보는 인덱스 3에 등장)
            right[int(info[0])] = int(info[3])  
    
    in_order(1)     # 순회 후 생성된 result 출력
    
    print(f'#{tc} {result}')