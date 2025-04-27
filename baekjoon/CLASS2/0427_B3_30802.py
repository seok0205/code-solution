'''
B3 30802 웰컴 키트

티셔츠 한장 펜 한 자루가 담긴 웰컴 키트를 나눠줄 예정

티셔츠는 S, M, L, XL, XXL, XXXL, 6가지 사이즈
티셔츠는 같은 사이즈 T장 묶음으로만 주문 가능

펜은 한종류, P자루씩 묶음으로 주문하거나 한 자루씩 주문 가능

N명의 참가자중 티셔츠를 신청한 사람은 각각 S명, M명, L명, XL명, XXL명, XXXL명임. 티셔츠는 남아도 됨.
부족해선 안됨. 신청한 사이즈대로 나눠주어야함.
펜은 남거나 부족하면 안되고 정확히 참가자 수만큼 준비해야함.

티셔츠 T장씩 최소 몇 묶음 주문해야 하는지, 펜을 P자루씩 몇 묶음 주문할 수 있고, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하는 문제

입력:
N: 참가자 수
S, M, L, XL, XXL, XXXL 신청자 수 공백두고 주어짐
T, P : 티셔츠와 펜의 묶음 수 공백두고 주어짐
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_result = 0

for shirt in shirts:        # 셔츠 사이즈당 몇 묶음 시켜야하는지 확인
    if shirt % T:           # 나머지 남으면 한묶음 더시킴
        shirt_result += (shirt // T + 1)
    else:                   # 알맞게 떨어지면 그만큼만 시킴
        shirt_result += shirt // T

print(shirt_result)
print(N//P, N%P)        # 펜 묶음 구하고, 나머지 구하기
