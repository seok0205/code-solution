'''
S4 9012 괄호

괄호 문자열은 두개 괄호기호 "()"로 이루어진 문자열 PS라 부름
올바르게 구성되면 VPS. ex) "()()", "(())()"

VPS인지 판단해서 YES, NO로 나타내는 문제

입력:
T : 테스트 케이스 개수
T줄동안 괄호문자열
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for _ in range(T):
    pstring = list(input())         # 괄호 받기
    stack = []                      # 괄호 확인할 스택

    if pstring[0] == ')':           # 첫 문자가 '('가 아니면 무조건 올바른 형태 아님
        print('NO')
        continue
    else:
        stack.append(pstring[0])    # 첫 '('를 스택에 넣고
        for i in range(1, len(pstring)):        # 다음 인덱스부터
            if pstring[i] == '(':               # '('가 또나오면 스택에 추가
                stack.append(pstring[i])
            else:                               # 만약 ')'가 나온다?
                if stack:                       # 스택에 '('가 있으면 짝맞으므로 '('를 꺼냄으로써 하나의 올바른 확인
                    stack.pop()
                else:                           # 만약 없는데 ')'가 나오면 올바른형태아님
                    result = 'NO'
                    break
        else:                                   # 막히는것없이 진행했는데
            if stack:                           # 스택에 남아있다? VPS 아님.짝못찾았단 소리
                result = 'NO'
            else:                               # 남아있는거 없으면 올바른 형태!
                result = 'YES'

    print(result)