'''
S3 2579 계단 오르기

문제 설명:
계단 아래 시작점부터 꼭대기에 위치한 도착점까지 가야함
계단에는 일정한 점수가 쓰여 있음. 밟으면 점수 획득
오를때 규칙이 존재
1. 계단은 한번에 하나 혹은 두 계단 오를 수 있음
2. 연속된 세 개의 계단을 모두 밟아선 안됨. 시작점은 포함 x
3. 마지막 도착 계단은 무조건 밟아야 함

각 계단의 쓰인 점수가 주어질때, 얻을 수 있는 총점수의 최댓값 구하는 문제

입력:
첫째 줄 계단 개수. 300이하 자연수.
둘째 줄 부터 한 줄에 하나씩 계단 점수 주어짐. 쓰인 점수는 10,000이하 자연수

출력:
총 점수의 최댓값 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
score = [0]
result = [0 for _ in range(N+1)]

for _ in range(N):
    s = int(input())
    score.append(s)

result[1] = score[1]
if N >= 2:
    result[2] = score[1] + score[2]
if N >= 3:
    for i in range(3, N+1):
        result[i] = max(result[i-3] + score[i-1] + score[i], result[i-2] + score[i])

print(str(result[-1]))