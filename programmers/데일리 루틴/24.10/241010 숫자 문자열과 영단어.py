def solution(s):
    number_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number = s  #eng리스트에 바꿔야할 문자열 저장 number에 입력받은 s 저장
    i = 0

    for j in number_eng:    #eng리스트에 있는 문자열 하나씩 비교
        number = number.replace(j, str(i))  #eng리스트에 있는 단어와 일치한다면 변경한다
        i += 1  #비교할 문자열 인덱스 증가

    return number

s = input()
print(solution(s))