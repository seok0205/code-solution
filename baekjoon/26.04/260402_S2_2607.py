'''
S2 2607 비슷한 단어

문제 설명:
영문 알파벳 대문자로 이루어진 두 단어가 두 조건 만족하면 같은 구성 갖는다 말함.

1. 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
2. 같은 문자는 같은 개수만큼 있다.

예로 'DOG'와 'GOD'는 둘 다 D, G, O 세 문자로 이루어져 있고, 양쪽 모두 하나씩 있으므로 같은 구성임.
하지만 'GOD', 'GOOD'의 경우 O의 개수가 달라 다른 구성임.

두단어가 같은 구성을 갖는 경우, 혹은 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한단어와 같은 구성을 갖는 경우는 비슷한 단어라고 함.

입력으로 여러개의 서로 다른 단어가 주어질 때, 첫번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램 작성.

입력:
첫째 줄 - 단어 개수
둘째 줄 - 한 줄에 하나의 단어.
모든 단어는 알파벳 대문자. 단어 개수는 100개 이하, 각 단어 길이는 10 이하.

출력:
입력으로 주어진 첫번째 단어와 비슷한 단어가 몇개인지 첫째 줄에 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

num = int(input())
main_dic = dict()
result = 0

for i in range(num):
    if i == 0:
        main_word = input().strip()
        for i in main_word:
            if i in main_dic:
                main_dic[i] += 1
            else:
                main_dic[i] = 1
    else:
        word = input().strip()
        sub_dic = main_dic.copy()
        word_list = list(word)
        temp = 0
        for k in range(len(word_list)):
            if temp > 1:
                break

            if word_list[k] in sub_dic and sub_dic[word_list[k]]:
                sub_dic[word_list[k]] -= 1
            else:
                temp += 1
        
        if sum(sub_dic.values()) > 1:
            continue

        if temp < 2:
            result += 1

print(result)