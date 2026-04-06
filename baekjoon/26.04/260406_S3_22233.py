'''
S3 22333 가희와 키워드

문제 설명:
블로그 운영 중.
블로그에 글을 쓰기 위해, 메모장에 키워드를 적곤 함.
지금까지 메모장에 써진 키워드는 모두 서로 다르고, 총 N개가 존재.
새로운 글 작성 시, 최대 10개의 키워드에 대해 글을 작성.

이 키워드들 중 메모장에 있었던 키워드는 가희가 글을 쓴 이후, 메모장에서 지워지게 됨.
블로그에 글을 쓰고 나서, 메모장에 있는 키워드가 몇 개인지 알고 싶음.

입력:
첫 줄 - 메모장에 적은 키워드 개수 N, 블로그에 쓴 글 개수 M.
둘째 줄 - 2번째 줄부터 N+1줄까지 메모장에 적은 키워드 N개 주어짐.
N+2번째 줄 부터 N+M+1줄 까지 가희가 쓴 글과 관련된 키워드가 쉼표를 기준으로 주어짐. 공백으로 구분되지 않음.
(1 <= N(M) <= 2 * 10**5, 1 <= 글에 있는 키워드 개수 <= 10, 1 <= 키워드 길이 <= 10)
키워드는 소문자와 숫자로만 이루어짐.
메모장에 있는 키워드 이름은 중복 X.
글에 있는 키워드 이름은 중복 X, 그러나, 한 키워드는 여러 글에 있을 수 있음.

출력:
x번째 줄에는 x번째 글을 쓰고 메모장에 남은 키워드 개수 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

word_dic = set()

for _ in range(N):
    word = input().strip()
    word_dic.add(word)

for _ in range(M):
    datas = list(input().strip().split(','))
    
    for data in datas:
        if data in word_dic:
            word_dic.discard(data)

    result = len(word_dic)
    print(result)