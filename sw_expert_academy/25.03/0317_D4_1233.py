'''
D4 1233 사칙연산 유효성 검사

사칙 연산으로 구성된 식은 이진 트리로 표현 가능
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의
결과를 사용해서 해당 연산자를 적용

사칙연산 +, -, /, *와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때,
이 식의 유효성을 검사하는 프로그램 작성(적절한 식인지 확인)

계산 가능하면 1, 불가능 시 0 출력, 0으로 나누는 경우 고려 X
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(idx):
    if idx > N:
        return
    
    if edge[idx]:
        x = edge[idx][0]
        cal(x)
        
    if tree[idx] == '+':
        pass
    
    if len(edge[idx]) == 2:
        y = edge[idx][1]
        cal(y)


for tc in range(1, 11):
    N = int(input())
    tree = [0]
    edge = [0]
    for _ in range(N):
        info = list(map(str, input().split()))
        tree.append(info[1])
        edge.append(info[2:])
    