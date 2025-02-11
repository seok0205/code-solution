'''
D1 9367 점점 커지는 당근의 개수

선별기는 연속으로 당근의 크기가 커진 경우 그 개수를 알려줌
당근의 크기가 수확한 순서로 주어질 때, 선별기로 연속으로 커지는 당근의 개수는 최대 얼마인지 출력
연속으로 커지지않는 경우 구간 최소 길이는 1
N개의 당근을 수확, 당근의 크기 C는 1부터 10까지의 정수로 정해짐

제약사항:
5 <= N <= 1000
1 <= C <= 10

입력:
T : tc 개수
N : 당근 개수
C : 당근의 크기 N개의 정수

출력:
연속으로 커지는 당근 개수 최대값
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    result = 1      # 최소 구간 길이 1
    max_length = 1  # 순회할 때마다 변하는 일시적 길이

    for i in range(N-1):    # 끝을 판단하고 길이 늘리기 때문에 -1
        if C[i+1] > C[i]:    # 만약 다음 인덱스가 현재 인덱스보다 크면
            max_length += 1     # 1 증가
        else:   # 이외에는
            result = max(result, max_length)    #최댓값 판별후
            max_length = 1      # 최댓값 초기화 1로.
    result = max(result, max_length)
    print(f'#{tc} {result}')
