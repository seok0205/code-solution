'''
2775 B1 부녀회장이 될테야

문제 설명:
아파트 거주 조건은 'a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.'
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정.
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    result = 0

    for i in range(k):
        pass