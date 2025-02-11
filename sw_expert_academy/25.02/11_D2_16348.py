'''
D2 16348 회문

어느 방향으로 읽어도 같은 문자열을 회문이라 함
NxN 글자판에서 길이가 M인 회문을 찾아 출력
회문은 1개 존재하고, 가로 뿐만 아니라 세로도 찾을 수 있음

입력:
N, M : 글자판 가로세로 길이, 찾으려는 회문 길이
다음 줄 부터 NxN 글ㅈ판
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    for i in range(N):      # 행
        for j in range(N-M+1):
            string_row = matrix[i][j:j+M]       # 탐색할 문자열

            for k in range(M//2):
                if string_row[k] != string_row[M-k-1]:  # 대응 되는 인덱스의 값이 다르면 값이 될 수 없음
                    break
            else:   # for문를 모두 실행했다면 회문임
                result = string_row

    for i in range(N):      # 열
        for j in range(N-M+1):
            string_col = list()
            for k in range(M):
                string_col.append(matrix[j + k][i])     # 탐색할 문자열

            for m in range(M//2):
                if string_col[m] != string_col[M-m-1]:  # 대응 되는 인덱스 값이 다르면 회문 아님
                    break
            else:
                result = string_col

    print(f"#{tc} {''.join(result)}")
