'''
S1 1283 단축키 지정

문제 설명:
한글 프로그램 메뉴에는 총 N개의 옵션.
각 옵션들은 한 개 혹은 여러 개의 단어로 옵션의 기능을 설명해놓음.
위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 함.

1. 먼저 하나의 옵션에 대해 왼쪽부터 오른쪽 순서로 단어의 첫 글짜가 이미 단축키로 지정되어 있는지 살핌. 만약 지정이 안되어 있따면 그 알파벳을 단축키로 지정.
2. 만약 모든 단어의 첫 글자가 이미 지정되어 있다면 왼쪽부터 차례대로 알파벳을 보면서 단축키로 지정 안된 것이 있다면 단축키로 지정.
3. 어떤 것도 단축키로 지정하지 못하면 그냥 놔두고, 대소문자 구분 x.
4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례로 적용.

입력:
첫 줄 - 옵션 개수 N (1 <= N <= 30).
둘째 줄부터 N + 1번째 줄 - 옵션을 나타내는 문자열.
하나의 옵션은 5개 이하의 단어로 표현. 각 단어 역시 10개 이하의 알파벳으로 표현.
단어는 공백 한 칸으로 구분.

출력:
N개의 줄에 각 옵션을 출력하는 데 단축키로 지정된 알파벳은 좌우에 [] 괄호 씌워서 표현.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
keys = [0] * N

for i in range(N):
    option = input().strip()
    temp = []

    words = option.split()

    for word in words:
        key = ord(word[0].upper())
        if keys[i] == 0 and key not in keys:
            keys[i] = key
            temp.append('[' + word[0] + ']' + word[1:])
        else:
            temp.append(word)

    if keys[i] == 0:
        temp.clear()

        for word in words:
            if keys[i]:
                temp.append(word)
                continue

            sub = []
            sub.append(word[0])

            for j in range(1, len(word)):
                key = ord(word[j].upper())

                if keys[i] == 0 and key not in keys:
                    keys[i] = key
                    sub.append('[' + word[j] + ']')
                else:
                    sub.append(word[j])
                
            temp.append(''.join(sub))

    print(' '.join(temp))