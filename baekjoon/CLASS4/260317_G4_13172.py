'''
G4 13172 시그마

문제 설명:
이제 이 방식으로 M 개의 주사위가 있고,
i번째 주사위가 Ni면체 주사위이며,
모든 면에 적힌 숫자를 더한 값이 Si일 때,
각 주사위에 대해서 주사위를 던졌을 때 주사위의 각 면이 나올 확률이 동일하다면,
모든 주사위를 한 번씩 던졌을 때 나온 숫자들의 합의 기댓값을 구하는 문제를 해결해보자.

입력:
첫 번째 줄에는 주사위의 수를 나타내는 정수 M(1 ≤ M ≤ 104)이 주어진다.
다음 M개의 줄은 각 주사위의 정보를 나타내며, 이 중 i(1 ≤ i ≤ M)번째 줄에는 Ni, Si(1 ≤ Ni, Si ≤ 109)가 공백으로 구분되어 주어진다.

출력:
모든 주사위를 한 번씩 던졌을 때 나온 숫자들의 합의 기댓값을 출력한다.
정확한 판별을 위해, 답을 기약분수로 나타내었을 때 a/b가 된다면, (a x b-1) mod 1,000,000,007을 대신 출력하도록 한다.
b-1은 b의 모듈러 곱셈에 대한 역원이다. 이 문제에서는 가능한 모든 입력에 대해 답이 존재한다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


M = int(input())
result = 0
mod = 1000000007

for _ in range(M):
    N, S = map(int, input().split())

    num = gcd(N, S)
    N //= num
    S //= num

    power = pow(N, mod - 2, mod)

    result = (result + (S * power)) % mod

output(str(result))