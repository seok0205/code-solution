'''
S3 1966 프린터 큐

문제 설명:
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO 인쇄

1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
    이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치, 그렇지 않다면 바로 인쇄

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄
현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄

입력:
첫 줄에 TC의 수. TC마다 두 줄로 이루어짐
첫 줄은 문서 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번 째인지 나타내는 정수 M
두번째 줄은 N개 문서의 중요도가 차례로 적힘. 1이상 9이하 정수. 같은 중요도도 존재.

출력:
각 TC에 대해 문서가 몇 번째로 인쇄되는지 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))

    result = 1
    while docs:
        if docs[0] < max(docs):
            docs.append(docs.pop(0))
        else:
            if M == 0:
                break
                
            docs.pop(0)
            result += 1
        
        if M > 0:
            M = M - 1
        else:
            M = len(docs) - 1

    print(result)