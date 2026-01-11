'''
B1 10989 수 정렬하기 3

N개의 수가 주어질 떄, 이를 오름차순을 정렬하는 프로그램 작성

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

count = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    for _ in range(count[i]):
        sys.stdout.write(f"{i}\n")