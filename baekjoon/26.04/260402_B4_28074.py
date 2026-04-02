'''
B4 28074 모비스

문제 설명:
스티커 문자중 'M', 'O', 'B', 'I', 'S'만 오려서 적절히 배치하려함.
스티커 용지에 인쇄되어 있는 문자열 주어짐.
이문자들을 활용해 MOBIS를 만들수 있나?

입력:
문자열. (1 <= 길이 <= 100).
알파벳 대문자로만 구성.

출력:
주어진 문자열에 포함된 알파벳 대문자들을 활용해 MOBIS를 만들 수 있으면 YES, 아니면 NO 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

string = input().strip()
word = ['M', 'O', 'B', 'I', 'S']

for i in string:
    if i in word:
        word.remove(i)
    
if word:
    print('NO')
else:
    print('YES')