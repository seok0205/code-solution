'''
S2 30804 과일 탕후루

문제 설명:
긴 막대에 N개의 과일이 꽂힌 탕후루 만듦
과일의 각 종류는 1부터 9까지 번호가 있음.
앞부터 차례로 S1~N 과일이 꽂힘.
주문이 과일을 두 종류 이하로 사용해달라는 요청이었음
막대의 앞과 뒤쪽에서 몇개의 과일을 빼서 두 종류 이하의 과일을 남기기로 함.
앞에서 a개, 뒤에서 b개를 빼면 N -(a+b)개가 꽂힌 탕후루가 된다.
두 종류 이하로 사용한 탕후루 중, 과일의 개수가 가장 많은 탕후루의 과일 개수 구하는 문제.

입력:
첫 줄 - N (1~200,000)
둘째 줄 - 탕후루에 꽂힌 과일을 의미하는 N개의 정수들이 공백으로 구분되어 주어짐

출력:
과일이 제일 많이 꽂힌 탕후루의 과일 개수 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input().strip())
tang = list(map(int, input().strip().split()))
s = 0
result = 0
fruit_dic = dict()

for i in range(N):
    now = tang[i]
    if now in fruit_dic:
        fruit_dic[now] += 1
    else:
        fruit_dic[now] = 1

    while len(fruit_dic) > 2:
        left = tang[s]
        fruit_dic[left] -= 1

        if fruit_dic[left] == 0:
            fruit_dic.pop(left)

        s += 1
    
    result = max(result, i-s+1)

output(str(result))