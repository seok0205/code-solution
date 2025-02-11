'''
D3 1221 GNS

0 ~ 9의 값을 영어로 나타낸 값이 있음
숫자 크기대로 정렬해서 출력하는 문제

입력:
테스트 케이스 개수
'#테스트케이스번호 테스트케이스길이(단어개수)'
테스트 케이스(단어와 단어 사이는 하나의 공백 구분)(100<=N<=10000)
'''

T = int(input())

# 딕셔너리에 각 문자를 키, 이에 해당하는 숫자를 밸류로 생성
word_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

for tc in range(1, T+1):
    tc_num, length = list(input().split())
    word = list(input().split())

    changed_num = list()

    for i in range(len(word)):
        changed_num.append(word_dic[word[i]])       # 새로 만든 changed_num에 문자에 맞는 밸류값으로(숫자로) 추가

    changed_num.sort()      # 정렬

    for i in range(len(changed_num)):
        for key, value in word_dic.items():     # 딕셔너리의 밸류값으로 키값을 찾아서 다시 changed_num의 원소들을 문자로 변경
            if value == changed_num[i]:         # 정렬된 상태로 나오게 됨
                changed_num[i] = key
    
    print(f'#{tc}')
    print(f"{' '.join(changed_num)}")