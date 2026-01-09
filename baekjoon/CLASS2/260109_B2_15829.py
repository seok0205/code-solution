'''
15829 B2 Hashing

문제 설명:
해시 함수는 임의의 길이의 입력을 받아서 고정된 길이의 출력을 보내는 함수.
자료의 저장과 탐색에 쓰임.

항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더하는 것은 해시 충돌을 방지하기 위한 좋은 방법.

계수와 나누는 큰 수는 서로소인 숫자로 정하는 것이 일반적. r의 값은 26보다 큰 소수인 31로하고 M의 값은 1234567891로 함.

입력:
첫 줄에는 문자열의 길이 L
둘째 줄에는 영문 소문자로만 이루어진 문자열

출력:
해시 함수와 입력을 사용해 계산한 해시 값을 정수로 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

L = int(input())
word = input()
mod = 1234567891

def solution(L, word):
    result = 0
    for i in range(0, L):
        temp = ord(word[i]) - 96    # 아스키코드 상으로 a는 97이므로 96을 빼면 1,2,3... 형태
        result += temp * 31 ** i
    return result

print(solution(L, word) % mod)