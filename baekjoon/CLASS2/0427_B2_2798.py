'''
B2 2798 블랙잭

카드의 합이 21을 넘지 않는 한도 내에서, 카드 합을 최대한 크게 만드는 게임.

새로운 룰:
각 카드에 양의 정수가 쓰여있음. 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓음. 딜러는 숫자 M을 외침.
제한된 시간안에 N장의 카드 중 3장을 고름. 플레이어가 고른 카드 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 함.

N장 카드에 쓰인 숫자가 주어질 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구하는 문제.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0      # 세 카드 합 담을 변수
cards.sort()        # 작은 수부터 정렬

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]       # 모든 경우의 수 돌아다니며 세 합 구함
            
            if card_sum <= M:                       # 합이 목표 수보다 작거나 같으면 result의 값과 비교 후 제일 큰값 집어넣음
                result = max(result, card_sum)
            else:                           # 작은수부터있기때문에 목표치보다 큰 값이 나오기 시작하면 그 뒤는 더 큰값임 그래서 break.
                break
            
print(result)