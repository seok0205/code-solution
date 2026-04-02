'''
B2 28114 팀명 정하기

문제 설명:
팀명을 지으려고 함. 가이드라인 존재.

1. 세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해 이어 붙인 문자열
2. 세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례로 나열한 문자열

세 팀원의 해결 문제 개수, 입학 연도, 성씨가 주어지면 1번 2번으로 만들어지는 팀명을 차례로 출력.

입력:
한줄당 한명의 정보가 주어짐
P, Y, S 가 공백을 두고 세 줄동안 주어짐.
(1 <= P <= 20000, 2010 <= Y <= 2099)
숫자와 성씨는 모두 다르다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

years = []
info = []

for _ in range(3):
    data = list(input().strip().split())
    P, Y, S = int(data[0]), int(data[1]), data[2]
    years.append(Y % 100)
    info.append((P, S))

years.sort()
print(''.join(map(str, years)))

info.sort(key=lambda x: -x[0])
name = ''

for num, last in info:
    name += last[0]

print(name)