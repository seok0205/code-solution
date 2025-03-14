'''
모의 SW 역량테스트 1952 수영장

난 지출이 너무 많아 내년 1년 동안 각 달의 이용 계획을 수립, 적은 비용으로 수영장 이용 방법 모색중

판매 이용권 4가지
1. 1일 이용권 : 1일 이용 가능
2. 1달 이용권 : 1달 동안 이용 가능. 매달 1일 시작
3. 3달 이용권 : 연속된 3달 동안 이용 가능. 매달 1일부터 시작
(11, 12월에도 사용은 가능/ 다음 해의 이용권만 구매할 수 있어서 3달이용권은 11, 12, 1월이나 12, 1, 2월동안 사용하도록 구매할 수 없음)
4. 1년 이용권 : 1년 동안 이용 가능. 매년 1월 1일 시작

이용계획이 주어짐. 나타나는 숫자는 해당 달에 수영장을 이용할 날의 수를 의미
각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')


def swimming_plan(type, cnt, cost):
    global result
    
    if cnt >= 12:               # 월수가 12개월이 넘어가면 결과(총합) 비교한후 적은것을 result에 대입
        if result > cost:
            result = cost
        return
    
    if cost > result:           # 가격이 이미 최솟값으로 설정되어있는 값 넘어가면 재귀 중단
        return
    
    if type == day:             # 1일 단위로 결제를 했을 때 한달 치 가격
        cost += schedule[cnt] * type
        cnt += 1                # 1개월 증가
    elif type == month:         # 한달 단위 결제 했을 때
        cost += type
        cnt += 1
    elif type == month_3:       # 3달치 결제 했을 때
        cost += type
        cnt += 3
    
    swimming_plan(day, cnt, cost)       # 다음 결제를 무엇으로 할지 선택
    swimming_plan(month, cnt, cost)
    swimming_plan(month_3, cnt, cost)


T = int(input())

for tc in range(1, T+1):
    day, month, month_3, year = map(int, input().split())
    schedule = list(map(int, input().split()))
    
    result = year           # 1년치 결제를 기준으로. 1년치는 어떤 테스트 케이스든 무조건 한번 결제이기 때문에 최솟값의 기준으로 설정
    
    swimming_plan(day, 0, 0)        # 첫 결제가 1일치인지, 한달치인지, 세달치인지 결정
    swimming_plan(month, 0, 0)
    swimming_plan(month_3, 0, 0)
    
    print(f'#{tc} {result}')
    
    # # DP식 풀이
    # # 이용권 가격들 (1일, 1달, 3달, 1년)
    # cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # # 12개월 이용 계획
    # days = [0] + list(map(int, input().split()))

    # dp = [0] * 13
    # # 시작점 초기화 (1월, 2월)
    # # 1월의 가격 (1일권 구매 vs 1달권 구매)
    # dp[1] = min(days[1] * cost_day, cost_month)
    # # 2월의 가격 = 1월의 가격 + (1일권 구매 vs 1달권 구매)
    # dp[2] = dp[1] + min(days[2] * cost_day, cost_month)

    # # 3월~12월은 반복하면서 계산
    # for month in range(3, 13):
    #     # N월의 최소 비용 후보
    #     # 1. (N-3)월에 3개월 이용권을 구입한 경우
    #     # 2. (N-1)월의 최소 비용 + 1일권 구매
    #     # 3. (N-1)월의 최소 비용 + 1달권 구매
    #     dp[month] = min(dp[month-3] + cost_month3
    #                     ,dp[month-1] + (days[month] * cost_day)
    #                     ,dp[month-1] + cost_month)

    # # 12월의 누적 최소 금액 vs 1년권
    # answer = min(dp[12], cost_year)
    # print(f'#{tc} {answer}')