# s의 문자열의 각 모든 문자를 index가 변수 index만큼 뒤에 있는 알파벳으로 변환하는 문제.
# skip에 있는 문자들은 모두 건너뛴다. 예를 들어 s가 'a'이고 skip이 'b', index가 2일때, s는 d로 변환된다.

s = 'aukks'
skip = 'wbqd'
index = 5

alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 순서
result = '' 

for i in skip:  # 알파벳 순서에서 건너뛰어야 하는 문자들 제거.
    alphabet = alphabet.replace(i, '')

for i in s:
    n = (alphabet.index(i) + index) % len(alphabet) # 알파벳의 변환값 구하기. alphabet 길이로 나눠 나머지를 구해 'z'의 인덱스를 넘어도 'a'로 돌아가도록 설정.
    result = ''.join([result, alphabet[n]]) # join활용해 result에 계속 추가.

print(result)