'''
D2 16811 당근 포장하기

N개 당근 주문 시 대, 중, 소로 구분해 포장

조건:
같은 크기 당근은 같은 상자에 있어야 함
비어 있는 상자 있으면 안됨
N/2를 초과하는(N이 홀수면 소수점 버림) 것도 안됨

각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 함
개수 차이를 서류에 표시

입력:
T : 수확 횟수
N : 당근 개수
C : 당근 크기

출력:
포장 할 수 없으면 -1, 포장할 수 있다면 상자에 든 당근의 개수 차이가 최소 일대 차이값 출력
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()        # 입력받은 당근 크기 정렬
    
    cnt = [0 for _ in range(N+1)]       # 같은 크기의 당근은 한 박스에 있어야 하므로 카운팅으로 합치기
    for i in C:
        cnt[i] += 1
    cnt = cnt[1:]       # 앞의 0은 제함

    min_length = 1000       # N 입력값 최대 값이 1000이어서 최대최소 차가 나오지않으면 바뀌지 않음

    for i in range(1, len(cnt)-1):      # 집합 3개의 경우의 수 위해 반복문 실행
        for j in range(i+1, len(cnt)):
            small, middle, big = cnt[:i], cnt[i:j], cnt[j:]     # 나눌 범위 분류(소, 중, 대)
            small_sum, middle_sum, big_sum = sum(small), sum(middle), sum(big)      # 경우의 수 하나 나올때마다 범위내 개수를 모두 합한 값 도출
            if 0 < small_sum <= N//2 and 0 < middle_sum <= N//2 and 0 < big_sum <= N//2:        # 박스에 하나는 들어있어야 하고, 박스 하나에 초과값 못들어가므로 조건 설정
                differ = max(small_sum, middle_sum, big_sum) - min(small_sum, middle_sum, big_sum)      # 최대, 최소 값 계산
                if min_length > differ:     # 최소값 비교 후 대입
                    min_length = differ

    if min_length == 1000:      # 최소값 바뀐 적 없으면 경우의수 없다는 것이므로 -1 출력
        min_length = -1

    print(f'#{tc} {min_length}')
