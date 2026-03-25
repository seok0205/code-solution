'''
G2 11444 피보나치 수 6

문제 설명:
피보나치 수는 0과 1로 시작.
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이됨.

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력:
첫째 줄에 n이 주어짐. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수.

출력:
첫째 줄에 n번째 피보나치 수를 1,000,000,007로 나눈 나머지 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

MOD = 1000000007


def find(a, b):
    visit = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                visit[i][j] = (visit[i][j] + a[i][k] * b[k][j]) % MOD
    return visit


def conquer(a, n):
    if n == 1:
        return a
    else:
        temp = conquer(a, n // 2)
        if n % 2 == 0:
            return find(temp, temp)
        else:
            return find(find(temp, temp), a)


n = int(input())
matrix = [[1, 1], [1, 0]]

if n == 0:
    output('0')
elif n == 1:
    output('1')
else:
    result = conquer(matrix, n)
    output(str(result[0][1]))