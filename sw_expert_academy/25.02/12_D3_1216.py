'''
D3 1216 회문 2

거꾸로 읽거나 똑바로 읽어도 같은 문장 혹은 단어를 회문이라 함
100x100 글자배열에서 가장 긴 회문을 구하는 문제
'''

import sys
sys.stdin = open('seok.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    matrix = [list(input()) for _ in range(100)]