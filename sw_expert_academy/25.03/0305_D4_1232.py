'''
D4 1232 사칙연산

이진 트리로 표현한 사칙연산. 임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와
오른쪽 서브 트리의 결과에 해당 연산자 적용.

사칙 연산과 양의 정수로만 구성된 임의의 이진 트리가 주어질때 이를 계산한 결과를 출력

입력:
10개의 테스트 케이스(총 테스트 케이스의 개수는 입력으로 주어지지 않는다)
각 테스트 케이스의 첫 줄에는 정점의 개수 N(1≤N≤1000)이 주어진다. 그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.
정점이 정수면 정점 번호와 양의 정수가 주어지고, 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
정점 번호는 1부터 N까지의 정수로 구분된고 루트 정점의 번호는 항상 1이다.
위의 예시에서, 숫자 4가 7번 정점에 해당하면 “7 4”으로 주어지고, 연산자 ‘/’가 2번 정점에 해당하면 두 자식이 각각 숫자 9인 4번 정점과 연산자 ‘-’인 5번 정점이므로 “2 / 4 5”로 주어진다.
'''


def calculate(T):       # 사칙연산 함수(후위연산 활용)
    if T:
        calculate(left[T])      # 왼쪽 수
        calculate(right[T])     # 오른쪽 수 확인 후
        if node[T] == '+':      # 현재노드의 연산자에 따라 상황에 맞게 계산(연산자아니면 그냥 넘어감. 숫자를 유지)
            node[T] = node[left[T]] + node[right[T]]
        elif node[T] == '-':
            node[T] = node[left[T]] - node[right[T]]
        elif node[T] == '*':
            node[T] = node[left[T]] * node[right[T]]
        elif node[T] == '/':
            node[T] = node[left[T]] // node[right[T]]
            

for tc in range(1, 11):
    N = int(input())
    
    node = [0] * (N+1)      # 각 노드에 저장된 값
    left = [0] * (N+1)      # 왼쪽 자식
    right = [0] * (N+1)     # 오른쪽 자식
    
    for i in range(N):
        info = list(map(str, input().split()))
        
        if info[1] in '+-/*':       # 만약 연산자가 나오면
            node[int(info[0])] = info[1]        # 문자열 유지한 채로 노드 저장값에 대입
        else:                       # 숫자가 나오면
            node[int(info[0])] = int(info[1])   # 정수 형태로 대입
        
        if info[1] in '+-/*':       # 연산자가 나왔다면 자식노드가 무조건 나옴
            left[int(info[0])] = int(info[2])       # 왼쪽 자식에 추가
            right[int(info[0])] = int(info[3])      # 오른쪽 자식 추가
            
    calculate(1)        # 루트노드에 최종 저장된값 구하려 함수 실행
            
    print(f'#{tc} {node[1]}')       # 바뀐 노드 저장값 리스트의 루트 노드 값 출력