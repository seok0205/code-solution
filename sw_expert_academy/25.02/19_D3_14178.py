'''
D3 14178 1차원 정원

1차원 수직선 위에 정원이 있음. 모든 정수 1 <= i <= N에 ㅔ대해 좌표 i 에 꽃이 하나씩 존재
분무기는 좌표마다 놓을 수 있고, 닫힌 구간 [x-D, x+D]에 심긴 모든 꽃에 물을 줄수 있음
모든 꽃이 한 개 이상의 분무기에서 물을 받을 수 있도록 하기 위해 필요한 최소한의 분무기 수 구하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    result = 0
    
    for i in range(1, N+1, M*2+1):  # 분무기 범위는 양방향으로 M만큼, 그리고 자기 자신.
        result += 1                 # 따라서 M*2+1이 범위, 최솟값은 겹치는 부분이 최대한 없어야 하므로
        
    print(f'#{tc} {result}')