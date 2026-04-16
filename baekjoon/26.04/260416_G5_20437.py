'''
G5 20437 문자열 게임 2

문제 설명:
문자열 게임이 있음.

1. 알파벳 소문자로 이루어진 문자열 W가 주어짐.
2. 양의 정수 K가 주어짐.
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이 구함.
4. 어떤 문자를 정확히 K개 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열 길이를 구함.

T번 진행.

입력:
문자열 게임의 수 T 주어짐. (1 <= T <= 100)
다음 줄부터 2개의 줄동안 문자열 W와 정수 K가 주어짐. (1 <= K <= |W| <= 10000)

출력:
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 두고 출력.
만약 만족하는 연속 문자열 없으면 -1 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input().strip()
    K = int(input())

    if K == 1:
        print(1, 1)
    else:
        spell_dict = dict()

        for i in range(len(W)):
            if W[i] not in spell_dict:
                spell_dict[W[i]] = []
            spell_dict[W[i]].append(i)

        min_val = float('inf')
        max_val = -1
        found = False

        for spell in spell_dict:
            temp = spell_dict[spell]

            if len(temp) >= K:
                found = True
                for i in range(len(temp) - K + 1):
                    length = temp[i+K-1] - temp[i] + 1

                    if length < min_val:
                        min_val = length
                    if length > max_val:
                        max_val = length

        if not found:
            print(-1)
        else:
            print(min_val, max_val)