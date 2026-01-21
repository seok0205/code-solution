'''
S3 11727 2xn 타일링 2

문제 설명:
2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수를 구하는 프로그램 작성.

입력:
첫째 줄에 n (1~1,000)

출력:
첫째 줄 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

result = [0] * (n+1)

if n >= 1:
    result[1] = 1
if n >= 2:
    result[2] = 3

for i in range(3, n+1):
    result[i] = result[i-1] + (2 * result[i-2])

print(str(result[n] % 10007))