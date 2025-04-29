'''
B1 11050 이항 계수 1

자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 구하는 문제

N은 1 이상 10이하, K는 0이상 N이하
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N, K = map(int, input().split())

sub_1 = 1       # N 팩토리얼

for i in range(N, 1, -1):
    sub_1 *= i

sub_2 = 1       # K 팩토리얼

for j in range(K, 1, -1):
    sub_2 *= j

sub_3 = 1       # N-K 팩토리얼

for k in range(N-K, 1, -1):
    sub_3 *= k

result = sub_1 // (sub_2 * sub_3)       # 이항 계수는 K팩토리얼 곱하기 N-K 팩토리얼 분의 N팩토리얼이다.

print(result)