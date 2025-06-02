'''
S3 11726 2xN 타일링

2xN 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 문제

첫째줄에 n 입력. 방법의 수를 10007로 나눈 나머지를 출력.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

result = [0, 1, 2]

for i in range(3, N+1):
    num = result[i-1] + result[i-2]
    result.append(num)

print(result[N]%10007)