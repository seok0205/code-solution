"""
D2 16311 특별한 정렬

N개의 정수가 주어지면 가장 큰수, 가장 작은수, 2번째 큰수, 2번째 작은수... 순으로 번갈아 정렬
10개까지 출력하는 문제

입력:
1 <= T <= 50
N = 정수 개수
ai = N개의 정수들
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()      # 정렬

    result = list()     # 결괏값이 될 리스트

    for i in range(5):      # 제일 큰 값 추가, 제일 작은 값 추가, 그 다음 큰값 추가, 그 다음 작은 값 추가... 10개까지...
        result.append(lst[N-1-i])   # 큰 값
        result.append(lst[i])   # 작은 값

    print(f"#{tc} {' '.join(map(str, result))}")