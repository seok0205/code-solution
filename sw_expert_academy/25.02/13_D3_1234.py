'''
D3 1234 비밀번호

0 ~ 9 문자열에서 같은 번호로 붙어있는 쌍들 제거, 남은 번호를 비밀번호로 출력
'''


def reduce_num(number):     # 같은 번호 붙은 쌍 제거 재귀 함수
    for i in range(len(number)-1):      # 숫자들을 순회하며
        if number[i] == number[i+1]:    # 만약 다음 숫자와 같으면
            number.pop(i+1)             # 다음 숫자 먼저 삭제(인덱스 문제로 이 구문이 먼저 실행되어야 함)
            number.pop(i)               # 현재 숫자 삭제
            break                       # 한 쌍 삭제 후 탈출
    else:                               # 만약 반복 숫자가 발견되지 않으면(for문이 정상적으로 break없이 실행되었을 때)
        return number                   # 그대로 숫자 출력
    return reduce_num(number)           # 반복숫자 발견시, 다음 반복숫자 발견 위해 재귀


T = 10

for tc in range(1, T+1):
    N, num = map(str, input().split())

    num = list(num)
    result = reduce_num(num)

    print(f'#{tc} {"".join(result)}')
