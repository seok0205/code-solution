'''
D2 2005 파스칼의 삼각형

크기가 N인 파스칼의 삼각형 만들어야 함
파스칼의 삼각형은 조건이 존재
1. 첫 번째 줄은 항상 1
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽, 오른쪽 위의 숫자의 합으로 구성됨
N 입력받아 크기 N인 파스칼 삼각형 출력하는 문제

제약:
파스칼 삼각형 크기는 1이상 10이하 정수

입력:
첫번째줄 T
각 테스트 케이스에는 N 주어짐

출력:
#t로 시작, 공백후 삼각형 각 줄의 처음 숫자가 나오기 전까지 공백 두고 출력
'''


def pascal(lst):    # 결과값들 담을 리스트 받음
    global cnt, N       # 크기가 1씩 증가하는 cnt, 구하려는 넓이값 N 글로벌 변수
    sub_lst = list()        # 한번 실행할때 얻을 리스트

    if cnt == 1:    # cnt가 1이면(첫번째 실행일때)
        lst.append([1])     # 1차원 리스트 1을 결과값에 넣음
    else:           # 첫번째 실행이 아니라면
        for i in range(cnt):
            if i == 0:      # 항상 파스칼 공식에서 양 끝은 1
                sub_lst.append(1)
            elif i == cnt-1:
                sub_lst.append(1)
            else:           # 삼각형 기준으로 윗줄의 본인 위치와 같은 인덱스와 이전의 인덱스의 합이 해당 인덱스의 값임
                sub_lst.append(sum(lst[cnt-2][i-1:i+1]))        # 결과 리스트에 저장되어 있는 값에서 찾아냄
        lst.append(sub_lst)     # 결과에 해당 cnt에서 얻은 리스트를 통째로 추가

    if cnt == N:        # cnt가 구하려는 크기인 N과 같으면 재귀 끝
        return
    cnt += 1        # N에 미치지 못하면 cnt 1 증가 후 재귀
    return pascal(lst)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = list()     # 결과담을 리스트 생성
    cnt = 1             # 1씩 증가하는 크기 1부터 시작. N의 최솟값이 1이기 때문

    pascal(result)

    print(f'#{tc}')
    for i in range(N):
        print(f'{" ".join(list(map(str, result[i])))}')
