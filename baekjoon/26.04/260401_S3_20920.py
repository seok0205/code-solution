'''
S3 20920 영단어 암기는 괴로워

문제 설명:
영어 시험에서 틀린 문제 바탕으로 암기하려고 함.
효율적으로 하기위해 단어장 만들려고함.
단어 순서는 우선순위가 차례로 적용되어 만들어짐.

1. 자주 나오는 단어일수로 앞에 배치
2. 해당 단어의 길이가 길수록 앞에 배치
3. 알파벳 사전 순으로 앞에 있는 단어일 수록 앞에 배치

M보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있어 길이가 M이상인 단어들만 외움.

입력:
첫째 줄 - 단어 개수 N, 단어 길이 기준 M (1 <= N <= 100,000, 1 <= M <= 10)
둘째 줄부터 N+1줄 까지 외울 단어 입력.
이때 입력은 알파벳 소문자만, 단어 길이는 10 넘지 않음.
단어장에 반드시 1개 이상 존재하는 입력만 주어짐.

출력:
단어장의 앞에 위치한 단어부터 한줄에 한단어씩 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
note_dic = dict()
note = []
for _ in range(N):
    word = input().strip()

    if len(word) < M:
        continue

    if word in note_dic:
        note_dic[word] += 1
    else:
        note_dic[word] = 1

for word, cnt in note_dic.items():
    note.append((word, cnt))

note.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, cnt in note:
    print(word)