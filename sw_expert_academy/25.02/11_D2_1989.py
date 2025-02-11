'''
D2 초심자의 회문 검사

거꾸로 읽어도 똑바로 읽어도 똑같은 문장이나 단어를 회문이라 함
단어를 입력받아 회문이면 1 출력, 아니면 0 출력

제약 사항:
3 이상 10 이하
'''

T = int(input())

for tc in range(1, T+1):
    word = list(input())

    result = 0

    for i in range(len(word)//2):       # 리스트로 만든 단어 배열에서 대응되는 인덱스의 동일 여부 판단
        if word[i] != word[len(word)-i-1]:
            break   # 같지 않으면 탈출
    else:   # 탈출 없이 그대로 빠져나온다면 동일한 단어인 회문
        result = 1

    print(f'#{tc} {result}')
