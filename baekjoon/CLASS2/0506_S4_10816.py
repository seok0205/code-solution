'''
S4 10816 숫자 카드 2

숫자 카드는 정수 하나가 적혀저 있는 카드.
숫자 카드 N개 보유중. M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇개 가지고 있는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
mycards = list(map(int, input().split()))

card_dic = dict()       # 카드 찾을 딕셔너리
result = [0] * M        # 결과 담을 리스트

for i in range(M):
    if mycards[i] in card_dic:      # 찾을 카드 딕셔너리에 모두 0으로 저장
        continue
    card_dic[mycards[i]] = 0

for i in range(N):
    if cards[i] in card_dic:        # 찾는 카드 있으면 딕셔너리 값 1 증가
        card_dic[cards[i]] += 1

for i in range(M):                  # 카드의 개수들 결과값에 저장
    result[i] = card_dic[mycards[i]]

print(" ".join(map(str, result)))       # 출력