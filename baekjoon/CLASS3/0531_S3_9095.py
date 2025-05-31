'''
S3 9095 1, 2, 3 더하기

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지
합을 나타낼 때는 수를 1개 이상 사용해야 함.

1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2
1, 3
3, 1

정수 n이 주어질 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 작성

케이스 개수 T 주어짐 각 테스트 케이스는 한줄, 정수 n은 양수, 11보다 작음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_expression(num, num_sum):
    global result

    if num_sum == num:      # num이 목표 값에 도달 하면 만들 수 있는 식 증가이므로 종료.
        result += 1
        return
    
    if num_sum > num:       # 목표치를 넘어가면 거기서 종료. 뺄셈은 없기 때문
        return
    
    make_expression(num, num_sum + 3)       # 다음 연산해보기
    make_expression(num, num_sum + 2)
    make_expression(num, num_sum + 1)


T = int(input())

for _ in range(T):
    N = int(input())

    result = 0

    make_expression(N, 0)
    print(result)