'''
S2 1654 랜선 자르기

문제 설명:
N개의 랜선을 만들어야 함.
원래 K개의 랜선을 가진 상태. 하지만 K개의 랜선은 길이가 제각각.
모두 N개의 같은 길이의 랜선으로 만들고 싶어서 K개의 랜선을 잘라서 만들어야 함.
예로, 300cm짜리 랜선에서 140cm 짜리 랜선을 두 개 자르면 20cm는 버려야 함.(이미 자른 건 못붙임)

랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정. 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정.
그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램 작성

입력:
첫째 줄 - K(1~10,000), N(1~1,000,000). 항상 K <= N
K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이(cm 단위) 랜선 길이는 2**31 -1 보다 작거나 같은 자연수

출력:
첫째 줄 - N개를 만들 수 있는 랜선의 최대 길이를 cm 단위의 정수로 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

K, N = map(int, input().strip().split())
lines = []

for _ in range(K):
    n = int(input())
    lines.append(n)

s = 1
e = max(lines)
result = 0

while s <= e:
    mid = (s+e) // 2

    cnt = 0
    for i in range(K):
        cnt += lines[i] // mid
    
    if cnt < N:
        e = mid - 1
    else:
        s = mid + 1
        result = mid

output(str(result))