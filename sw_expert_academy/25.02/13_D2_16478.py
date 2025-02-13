'''
D2 16478 반복문자 지우기

문자열 s에서 반복된 문자 지우려고 함. 지워진 부분은 다시 앞뒤를 연결함. 연결에 의해 반복문자가 생기면
그 부분도 다시 지움.
반복문자 지운 후 남은 문자열 길이를 출력하라. 남지 않으면 0 출력
'''


def reduce_string(s):       # 반복 문자 지우는 재귀함수
    for i in range(len(s)-1):       # 주어진 문자열을 순회하면서
        if s[i] == s[i+1]:      # 현재 문자가 다음 문자와 같으면
            s.pop(i+1)          # s에서 뒤에 문자 먼저 삭제한 다음
            s.pop(i)            # 현재 문자 삭제(차례바뀌면 다른 값이 삭제됨. 뒤 인덱스가 바뀌기 때문.)
            break               # 한 반복문자 삭제 시 탈출
    else:       # 반복문자 발견되지 않으면
        return s    # 문자열 그대로 출력
    return reduce_string(s)     # 반복문자가 삭제되어 탈출되면, 재귀


T = int(input())

for tc in range(1, T+1):
    string = list(input())

    result = len(reduce_string(string))

    print(f'#{tc} {result}')
