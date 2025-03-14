'''
D3 2817 부분 수열의 합

N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택해 그 합이 K가 되는 경우의 수를 구하시오
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def add(cnt, s):
    global result
    
    if s == K:              # 합이 K와 같으면 결과 1 증가하고 함수 종료
        result += 1
        return
    
    if s > K:               # K보다 합이 이미 큰 경우 함수 종료
        return
    
    if cnt == N:            # 모든 수를 봤다면 함수 종료
        return
    
    add(cnt+1, s + A[cnt])  # 해당 수를 합에 포함시키거나 안시키거나.
    add(cnt+1, s)
    

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = 0
    
    add(0, 0)
    
    print(f'#{tc} {result}')