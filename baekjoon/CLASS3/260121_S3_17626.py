'''
S3 17626 Four Squares

문제 설명:
모든 자연수는 넷 혹은 그이하의 제곱수의 합으로 표현할 수 있다고 증명됨
어떤 자연수는 복수의 방법으로 표현.
예로 26은 5의 제곱, 1의 제곱 함. 또한 4의 제곱, 3의 제곱, 1의 제곱의 합으로 표현 가능.
자연수 n이 주어질 때, 최소 개수의 제곱수 합으로 표현하는 프로그램 작성

입력:
입력은 자연수 n을 포함하는 한 줄로 구성 (1~50,000)

출력:
합이 n과 같게 되는 제곱수들의 최소 개수 한 줄에 출력
'''

import sys
import math
# sys.stdin=open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

def is_square(n):
    if n < 0:
        return False
    num = math.isqrt(n)
    return num * num == n

def solution():
    n = int(input())

    if is_square(n):
        return 1
    
    for i in range(1, math.isqrt(n)+1):
        if is_square(n - i*i):
            return 2
        
    for j in range(1, math.isqrt(n)+1):
        for k in range(1, math.isqrt(n - j*j)+1):
            if is_square(n - j*j - k*k):
                return 3
    
    return 4

result = solution()
print(str(result))