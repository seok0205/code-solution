'''
B2 8958 OX퀴즈

"OOXXOXXOOO"와 같은 OX퀴즈 결과. O는 정답, X는 오답. 문제를 맞은 경우 그 문제의
점수는 그 문제까지 연속된 O의 개수가 됨. 예로 위 문제는 10번문제가 3점.
총 점수는 10점임.

위 방식대로 점수 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for _ in range(T):
    quiz = input()
    
    result = 0
    sub = 0

    for i in quiz:
        if i == 'O':
            sub += 1        # 연속된 O의 점수 증가
            result += sub   # 총 점수에 추가.
        else:
            sub = 0     # 연속이 끊기면 연속 점수 초기화
    
    print(result)