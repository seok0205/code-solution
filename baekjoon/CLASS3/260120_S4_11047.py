'''
S4 11047 동전 0

문제 설명:
가지고 있는 동전은 총 N종류, 각 동전을 매우 많이 가지고 있는상태.
적절히 사용해 그 가치의 합을 K로 만들려고 함.
이때 필요한 동전 개수의 최솟값 구하는 프로그램 작성.

입력:
첫째 줄 N(1 ~ 10), K(1 ~ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어짐(가치는 1 ~ 1,000,000)
A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수

출력:
K원을 만드는 데 필요한 동전 개수의 최솟값 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
price = []
result = 0

for _ in range(N):
    a = int(input())
    price.append(a)

for i in range(N-1, -1, -1):
    cnt = K // price[i]
    K -= price[i] * cnt
    result += cnt

print(str(result))