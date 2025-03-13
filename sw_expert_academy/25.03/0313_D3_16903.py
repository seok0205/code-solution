'''
D3 16903 컨테이너 운반

화물에 실린 N개의 컨테이너를 M대의 트럭으로 A에서 B로 운반하려 함

트럭당 한 개의 컨테이너 운반 가능, 트럭의 적재용량 초과하는 컨테이너 운반 불가

컨테이너마다 실린 화물 무게, 트럭마다의 적재용량 주어짐
최대 M대의 트럭이 편도로 한번만 운행

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너 옮겼다면, 옮겨진 화물의
전체 무게가 얼마인지 구하는 문제

화물을 싣지 못한 트럭이 있을 수 있고, 남는 화물도 있을 수 있음.
컨테이너 한 개도 옮길 수 없는 경우 0 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    
    weight.sort(reverse=True)       # 제일 큰 값들로 정렬
    truck.sort(reverse=True)
    
    total = 0       # 옮긴 화물 무게
    w_idx = 0       # 화물 순서(인덱스)
    t_idx = 0       # 실어야할 트럭 순서
    
    while True:
        if w_idx == N or t_idx == M:    # 모든 화물을 운반했거나, 운반할 트럭이 없다면 탈출
            break
        
        if weight[w_idx] <= truck[t_idx]:   # 만약 트럭의 적재가능량이 화물의 무게보다 크면
            total += weight[w_idx]          # 운반
            t_idx += 1                      # 트럭당 하나 화물만 가능하므로 다음 트럭
            w_idx += 1                      # 다음 화물
        else:                               # 화물이 적재가능량보다 크면 다음 작은 화물 운반 시도
            w_idx += 1
    
    print(f'#{tc} {total}')