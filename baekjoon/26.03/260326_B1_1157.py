'''
B1 1157 단어 공부(복습)

문제 설명:
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이쓴 알파벳이 무엇인지 알아내는 프로그램. 대소문자 구분 X.

입력:
첫째 쭐에 알파벳 대소문자로 이루어진 단어 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

string = input().strip().upper()
dic_list = [0] * 26

for i in string:
    dic_list[ord(i)-65] += 1

cnt = 0
max_cnt = max(dic_list)
for i in range(26):
    if dic_list[i] == max_cnt:
        result = i
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(chr(result+65))