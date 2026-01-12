'''
B1 14626 ISBN

문제 설명:
ISBN은 전 세계 모든 도서에 부여된 고유번호로, 국제 표준 도서번호.
국가명, 발행자 등의 정보가 13자리의 숫자로 표시되어 있음.
마지막 숫자는 체크기호로, ISBN의 정확성 여부를 점검할 수 있는 숫자.
일련번호의 앞에서부터 각 자리마다 가중치 1, 3, 1, 3... 를 곱한 것을 모두 더하고, 그값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용.

ISBN이 abcdefghijklm 일 때, a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)
즉, 체크기호 m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10 이다.
단, 10으로 나눈 나머지 값이 0일 경우 체크기호는 0이다.

손상된 자리의 숫자를 찾아내는 프로그램 작성하는 문제

입력: ISBN 13자리 숫자가 입력된다. 훼손된 숫자는 *로 표시한다. (훼손된 일련번호는 체크기호를 제외한 무작위 한 자리이다.)
출력: 훼손된 숫자 *에 알맞은 숫자를 출력한다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

isbn = list(input())[:-1]
result = 0

for i in range(len(isbn)):
    if isbn[i] == '*':
        isbn[i] = result
        result = i
        continue
    else:
        if i % 2:
            isbn[i] = int(isbn[i]) * 3
        else:
            isbn[i] = int(isbn[i])

num = 0

while sum(isbn) % 10:
    num += 1
    if result % 2:
        isbn[result] = (num * 3)
    else:
        isbn[result] = num

print(num)