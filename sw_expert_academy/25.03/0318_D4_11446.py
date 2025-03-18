'''
D4 11446 사탕 가방

N종류의 사탕이 있고, 각 종류마다 AN개의 사탕이 있음
이 사탕을 가방에 잘 나눠 넣고 싶은데 다음 조건을 만족해야함

1. 가방 안에 정확히 M개의 사탕이 들어 있어야 함
2. 모든 가방에 들어있는 사탕 종류의 구성이 같아야 함

최대 몇 개의 사탕 가방을 만들 수 있는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    candys = list(map(int, input().split()))
    
    min_bag = 1
    max_bag = max(candys)
    
    # 최댓 최솟값이 같을 때까지 반복
    while min_bag <= max_bag:
        mid = (min_bag + max_bag) // 2  # 가방의 갯수
        cnt = 0                         # 가방하나에 들어가는 사탕 갯수
        for candy in candys:            # 사탕 갯수 // 가방 갯수 모두 더하기(이것으로 값이 가방하나에 든 사탕 개수 알수 있음)
            cnt += candy // mid
            
        if cnt < M:                     # M보다 가방하나에 들어가는 사탕 수인 cnt가 더 작으면 있는 가방에 다 안들어가는 것
            max_bag = mid - 1           # 최댓값 감소
        else:                           # M보다 커서 사탕이 남으면
            min_bag = mid + 1           # 최솟값 증가
    
    print(f'#{tc} {max_bag}')