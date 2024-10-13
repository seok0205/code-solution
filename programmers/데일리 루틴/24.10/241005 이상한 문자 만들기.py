def solution(s):
    array = s.split(' ')    #공백을 기준으로 단어 분리
    s_1 = ''    #변환 마친 문자열 저장할 변수
    
    for i in array:
        for j in range(len(i)):
            if j % 2 == 0:  #인젝스가 짝수라면 대문자화
                s_1 += i[j].upper()
            else:   #홀수라면 소문자화
                s_1 += i[j].lower()
        s_1 += ' '  #단어하나 변환 마칠때마다 공백.
    return s_1[:-1] #마지막 단어뒤에 공백이 하나 추가되므로 마지막 인덱스만 빼고 출력.

s = input() #문자열 입력
print(solution(s))