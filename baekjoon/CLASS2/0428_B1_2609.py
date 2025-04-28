'''
B1 2609 최대공약수와 최소공배수

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

A, B = map(int, input().split())

greatest_common_divisor = 0     # 최대공약수
idx = min(A, B)                 # 둘 중 작은 수부터 1씩 줄여나가기

while True:
    sub_a = A % idx     # 나머지를 구함. 0이면 나누어 떨어지는 것
    sub_b = B % idx

    if sub_a == 0 and sub_b == 0:       # 둘다 나누어 떨어지면 공약수 조건 만족
        greatest_common_divisor = idx
        break

    idx -= 1

a_num = list()
b_num = list()
idx = 0

while True:
    idx += 1
    a_num.append(A*idx)     # 1씩 늘려가면서 곱해봄
    b_num.append(B*idx)

    if A*idx in b_num:          # 나온수가 이미 b리스트에 있으면 그게 최소공배수!
        least_common_multiple = A*idx
        break

    if B*idx in a_num:          # 나온수가 이미 a리스트에 있으면 그게 최소공배수!
        least_common_multiple = B*idx
        break

print(greatest_common_divisor)
print(least_common_multiple)