'''
D3 16904 화물 도크

24시간 운영 물류센터에 화물 싣고 내리는 도크 설치되있음
0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가
화물을 싣고 내릴 수 있또록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있음
앞 작업의 종료와 동시에 다음 작업을 시작 할 수 있음

예로 앞 작업 종료 시간이 5시면 다음 작업 시작 시간은 5시부터 가능
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        s, e = map(int, input().split())
        time.append((e-s, s, e))        # 시간 차와 시작 시간, 끝나는 시간
        
    time.sort()     # 시간 차 순으로 정렬
    result = []     # 화물 작업 스케줄
    cnt = 0         # 화물차량 작업 횟수
    
    for i in time:      # 모든 신청서를 탐색
        for j in range(i[1], i[2]):     # 시간범위가
            if j in result:             # 스케줄 시간 겹치면 다음 신청서 확인
                break
        else:
            result.extend(list(range(i[1], i[2])))      # 안겹치면 스케줄 잡고, 횟수 증가
            cnt += 1
        
    print(f'#{tc} {cnt}')