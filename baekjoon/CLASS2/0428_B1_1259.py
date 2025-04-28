'''
B1 1259 팰린드롬수

어떤 단어를 뒤에서부터 읽어도 똑같다면 팰린드롬이라 함.
ex) radar, sees

수도 팰린드롬으로 취급 가능.
ex) 121, 12421

123, 1231은 팰린드롬수가 아님.
무의미한 0은 올수 없음.

각 줄마다 주어진 수가 팰린드롬수면 yes, 아니면 no 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

while True:
    num = input()

    if num == '0':
        break
    else:
        num = list(num)
        reversed_num = list(reversed(num))  # 리스트화 후 뒤집어서

        if num == reversed_num:     # 같으면 팰린드롬수
            print('yes')
        else:                       # 다르면 아님
            print('no')