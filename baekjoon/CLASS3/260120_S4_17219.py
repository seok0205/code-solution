'''
S4 17219 비밀번호 찾기

문제 설명:
메모장에 저장된 사이트의 주소, 비밀번호를 찾는 프로그램 작성

입력:
첫째 줄 저장된 사이트의 수 N (1~100,000), 비번 찾으려는 사이트 주소 M(1~100,000)
두번째 줄부터 N줄에 걸쳐 각 줄에 사이트 주소, 비밀번호가 공백으로 구분되어 주어짐
사이트 주소는 알파벳 소문자, 대분자, '-', '.'로 이루어지며, 중복 없음.
비밀번호는 대문자로만. 모두 길이는 최대 20자
N+2번째 줄부턴 M개의 줄에 걸쳐 비밀번호 찾으려는 사이트 주소가 하나씩 입력.(저장된 주소중에서만)

출력:
첫 줄부터 M개의 줄에 걸쳐 해당사이트의 비밀번호가 하나씩 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
memo = dict()

for _ in range(N):
    address, password = map(str, input().strip().split())
    memo[address] = password

for _ in range(M):
    address = input().strip()
    print(memo[address] + '\n')