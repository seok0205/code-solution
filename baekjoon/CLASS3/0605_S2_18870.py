'''
S2 18870 좌표 압축

수직선 위에 N개의 좌표 존재. 좌표 압축 적용하려 함.
Xi를 좌표 압축한 결과 X'i의 값은 Xi>Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 함.
X1, X2, ..., Xn에 좌표 압축 적용한 결과 X'1, X'2, ..., X'n을 출력.

입력:
첫 줄 - N
둘째 줄 - 공백으로 구분된 X1 ~ Xn.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
xy = list(map(int, input().split()))
xy_dic = dict()         # 좌표 압축한 값 저장할 딕셔너리

xy_set = list(set(xy))      # set으로 중복없애고 정렬함
xy_set.sort()

for i in range(len(xy_set)):        # 순서대로 딕셔너리에 대입. 오름차순이므로 i를 그대로 대입하면 좌표 압축 값.
    if xy_set[i] not in xy_dic:
        xy_dic[xy_set[i]] = i

for i in range(N):          # 원래 리스트에 그대로 딕셔너리값들로 대체
    xy[i] = xy_dic[xy[i]]

print(' '.join(map(str, xy)))           # 출력.