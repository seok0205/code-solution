'''
D3 10726 이진수 표현

정수 N, M이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지
판별하여 출력 마지막 N개의 비트 켜져 있으면 ON, 아니면 OFF 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    M = bin(M)      # 이진수로 나타냄
    target = M[2:]  # 이진수 표현 수식어인 0b 빼고 확인
    
    if len(target) < N: # target의 길이가 비트확인 N보다 작으면 0이 무조건 포함된다는 소리이므로 OFF
        result = 'OFF'
    else:               # 그렇지 않다면 뒤에서부터 확인
        for i in range(N):
            if target[len(target)-1-i] == '0':  # 0이면 OFF
                result = 'OFF'
                break
        else:           # N번 반복했는데 break걸리지 않는다면 모두 1이란 소리
            result = 'ON'
    
    print(f'#{tc} {result}')

    