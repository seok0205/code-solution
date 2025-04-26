'''
S5 1181 단어 정렬

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 문제

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

단, 중복된 단어는 하나만 남기고 제거해야 함

입력:
N : 단어 개수
N줄 동안 단어 주어짐
주어진 문자열의 길이는 50을 넘지 않음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())

string_list = list()

for _ in range(N):      # 입력 받은 문자열 리스트에 추가
    string = input()
    string_list.append(string)

new_string_list = list(set(string_list))        # set으로 중복 단어 삭제
new_string_list.sort()                          # 먼저 철자순으로 정렬하고,
new_string_list.sort(key = lambda x: len(x))    # 길이 순으로 정렬.

for i in new_string_list:       # 차례로 출력
    print(i)