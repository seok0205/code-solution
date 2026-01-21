'''
S3 9375 패션왕 신해빈

해빈이는 패션에 민감. 한번 입었던 옷들의 조합은 절대 입지 않음
안경, 코트, 상의, 신발 입으면 다음날은 무조건 바지를 추가로 입거나 안경대신 렌즈 착용해야함.
의상들이 주어졌을 때, 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐수 있나?

입력:
첫째 줄 - tc개수 최대 100
각 tc의 첫 줄 - 가진 의상 수 0~30
다음 n줄에는 가진 의상의 이름과 종류가 공백을 구분되어 주어짐. 같은 종류 의상은 하나만 착용 가능.
모든 문자열은 1~20자 알파벳 소문자. 같은 이름 의상 존재 x.

출력:
tc마다 의상 입을 수 있는 경우의 수 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    N = int(input())
    clothes = dict()

    for _ in range(N):
        clothes_name, clothes_type = map(str, input().strip().split())
        if clothes_type not in clothes:
            clothes[clothes_type] = 1
        else:
            clothes[clothes_type] += 1
    
    if len(clothes) > 1:
        result = 1
        for i in clothes.values():
            result *= (i+1)
        print(str(result - 1) + '\n')
    else:
        print(str(N) + '\n')