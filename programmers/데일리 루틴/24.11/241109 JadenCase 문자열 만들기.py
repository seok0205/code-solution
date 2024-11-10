'''
JadenCase는 모든 단어의 첫 문자가 대문자이고, 나머지 알파벳은 모두 소문자인 문자열.
첫 문자가 알파벳이 아니고 숫자일때는 이어지는 알파벳은 모두 소문자로 쓰면 됨.
주어진 문자열 s를 JadenCase로 바꾼 문자열을 구하라.

조건 :
숫자는 단어의 첫 문자로만 나옴.
숫자로만 이뤄진 단어는 없음.
공백문자가 연속해서 나올 수 있다.
'''

s = "3people unFollowed   me"

result = [] # JadenCase 문자열로 바꾼 단어 저장소
words = s.split(' ')    # 주어진 s를 공백을 단위로 분할

for i in words: # 분할한 단어 하나씩 JadenCase화
    if i:   # 공백문자가 연속해서 나올 수 있어서 조건을 넣었다. 이 조건을 넣지 않으면 공백문자 차례일때 슬라이싱 인덱스 오류 발생.
        result.append(i[0].upper() + i[1:].lower())
    else:   # 공백문자는 그냥 추가.
        result.append(i)

print(result)

print(' '.join(result))