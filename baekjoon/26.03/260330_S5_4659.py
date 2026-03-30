'''
S5 4659 비밀번호 발음하기

문제 설명:
패스워드 생성기 만들려고 계획중.
높은 품질의 비밀번호 조건.

1. 모음(a, e, i, o, u) 하나를 반드시 포함
2. 모음이 3개 혹은 자음이 3개 연속 오면 안됨.
3. 같은 글자 연속적으로 두번 오면 안되지만, ee, oo는 허용.

입력:
각 테스트 케이스는 한 줄로 이루어짐. 각 줄에 테스트할 패스워드가 주어짐.
마지막 테스트 케이스는 end이고, 패스워드는 한글자 이상 20글자 이하의 문자열. 또한 패스워드는 대문자 포함 X.

출력:
각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하라.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

dic = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input().strip()
    
    if word == 'end':
        break

    result = True
    one = False
    temp_two = 1
    temp_three = 1
    for i in range(len(word)):
        if one != True:
            if word[i] in dic:
                one = True
        if i != 0:
            if word[i-1] == word[i]:
                temp_three += 1
            else:
                temp_three = 1

            if temp_three == 2 and word[i] not in ['e', 'o']:
                result = False
                break
        
        if i != 0:
            if word[i-1] in dic:
                a = True
            else:
                a = False
            
            if word[i] in dic:
                b = True
            else:
                b = False

            if a == b:
                temp_two += 1
            else:
                temp_two = 1

            if temp_two == 3:
                result = False
                break
    
    if one and result:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")