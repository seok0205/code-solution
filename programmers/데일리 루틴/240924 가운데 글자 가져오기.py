def solution(s):
    if len(s) % 2 == 0: #문자열의 길이가 짝수라면, 문자열의 중간 두 글자 출력.
        a = len(s) / 2
        return s[int(a)-1:int(a)+1] #중간 두 글자 슬라이싱.
    elif len(s) % 2 == 1:   #문자열 길이가 홀수라면, 문자열 중간 한 글자 출력.
        a = len(s) // 2
        return s[a] #a는 중간 인덱스.

s = input()
print(solution(s))