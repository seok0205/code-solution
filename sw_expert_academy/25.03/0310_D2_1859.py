'''
D2 1859 백만 장자 프로젝트

조건:
연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음
하루에 최대 1만큼 구입 가능
판매는 얼마든지 가능

입력:
첫줄은 T
테스트 케이스 별로 첫줄은 자연수 N
둘째 줄은 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어짐
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    result = 0                                  # 최종 수익
    
    while True:
        if len(cost) == 0:                      # 주어진 가격 리스트가 없어질 때까지 반복
            break
        
        max_num = max(cost)                     # 주어진 가격 리스트중 가장 비싼 가격
        cost_sum = 0
        for i in range(len(cost)):              # 주어진 가격 리스트 순회하면서
            if cost[i] == max_num:              # 가장 비싼 가격 만나면
                cut = i                         # 위치 기억 후 반복 종료
                break
            else:                               # 만약 비싼 가격 아직 아니라면
                cost_sum += cost[i]             # 매매시 가격 누적 합
        
        result = result + (max_num * i) - cost_sum      # 이때까지 매수한 물건들 최댓값으로 모조리 팔고, 매매시 축적된 가격 빼면 수익
        cost = cost[cut+1:]             # 판매한 날 까지 리스트에서 삭제
    
    print(f'#{tc} {result}')