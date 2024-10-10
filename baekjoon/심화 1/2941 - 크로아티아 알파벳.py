croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
print(len(word))

#크로아티아 알파벳 예시 리스트 생성
#알파벳으로 구성된 문자열 입력

#예시 리스트 개수만큼 반복 확인 후 맞는 단어 발견시 *로 변경.
#str.replace()활용

#*들로 바뀐 word 문자열의 길이 출력.(=단어 개수)