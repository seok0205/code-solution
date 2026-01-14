'''
S5 1676 팩토리얼 0의 개수

문제설명:
N! 에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램 작성.

입력:
N (0보다 크거나 같고, 500보다 작거나 같음)

출력:
첫째 줄에 구한 0의 개수 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
num = 1

for i in range(1, N+1):
    num *= i

result = 0

for j in range(len(str(num))-1, -1, -1):
    if str(num)[j] == '0':
        result += 1
    else:
        print(result)
        break