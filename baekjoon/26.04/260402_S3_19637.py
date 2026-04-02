'''
S3 19637 IF문 좀 대신 써줘

문제 설명:
게임 개발자인 밀리는 전투력 시스템을 만들어, 캐릭터의 전투력을 기준으로 칭호 붙이려고 함.
예로, 전투력 10,000 이하의 캐릭터는 WEAK, 10,000초과, 100,000이하 캐릭터는 NORMAL, 100,000 초과, 1,000,000 이하 캐릭터는 STRONG임.
캐릭터의 전투력에 맞는 칭호 출력하는 프로그램 작성.

입력:
첫 줄 - 칭호 개수 N(1 <= N <= 10**5), 칭호출력 캐릭터 개수 M(1 <= M <= 10**5) 빈칸 두고 주어짐.
두번째 줄부터 N개의 줄에 강 칭호 이름 나타내는 길이 1이상, 11이하의 영어 대문자로만 구성된 문자열, 전투력 상한값을 나타내는 10**9이하의 음이 아닌 정수가 주어짐.
칭호는 전투력 상한값의 비내림차순으로 주어짐.
N+2번째 줄부터 M개의 각 줄에는 캐릭터의 전투력을 나타내는 음이 아닌 정수가 주어짐.
해당하는 칭호가 없는 전투력은 입력으로 주어지지 않음.

출력:
M개의 줄에 걸쳐 캐릭터 전투력에 맞는 칭호 순서대로 출력. 어떤 캐릭터의 전투력으로 출력할 수 있는 여러개면 가장 먼저 입력된 칭호 하나만 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
name_dic = list()

for _ in range(N):
    data = list(map(str, input().strip().split()))
    name, limit = data[0], int(data[1])
    name_dic.append((limit, name))

for _ in range(M):
    power = int(input())

    low = 0
    high = N-1
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if name_dic[mid][0] >= power:
            high = mid - 1
            result = mid  
        else:
            low = mid + 1

    print(name_dic[result][1])