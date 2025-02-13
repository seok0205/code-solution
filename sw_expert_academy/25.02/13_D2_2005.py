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


def pascal(lst):
    global cnt, N
    sub_lst = list()

    if cnt == 1:
        lst.append([1])
    else:
        for i in range(cnt):
            if i == 0:
                sub_lst.append(1)
            elif i == cnt-1:
                sub_lst.append(1)
            else:
                sub_lst.append(sum(lst[cnt-2][i-1:i+1]))
        lst.append(sub_lst)

    if cnt == N:
        return
    cnt += 1
    return pascal(lst)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = list()
    cnt = 1

    pascal(result)

    print(f'#{tc}')
    for i in range(N):
        print(f'{" ".join(list(map(str, result[i])))}')
