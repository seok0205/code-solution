'''
S3 20310 타노스

문제 설명:
0과 1로 이루어진 문자열 S를 봄.
신기하게 S가 포함하는 0의 개수와 S가 포함하는 1의 개수는 모두 짝수.
갑자기 S를 구성하는 문자 중 절반의 0과 1을 제거하여 새로운 문자열 S를 만들려고 함.
S로 가능한 문자열중 사전순으로 가장 빠른 것을 구하는 문제.

입력:
S의 길이는 2이상 500이하.
S는 짝수 개의 0과 짝수 개의 1로 이루어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

S = input().strip()
zero = S.count('0') // 2
one = S.count('1') // 2

zero_cnt = 0
one_cnt = 0

a = ''
for i in range(len(S)):
    if S[i] == '1' and one_cnt < one:
        one_cnt += 1
        continue
    
    a += S[i]

result = ''
for i in range(len(a)-1, -1, -1):
    if a[i] == '0' and zero_cnt < zero:
        zero_cnt += 1
        continue

    result = a[i] + result

print(result)