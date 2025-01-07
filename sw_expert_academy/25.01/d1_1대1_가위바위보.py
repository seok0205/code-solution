'''
A, B가 가위바위보를 함
가위는 1, 바위는 2, 보는 3으로 표현, A와 B는 무엇을 냈는지 입력으로 주어짐
A, B중 누가 이겼는지 판별하는 프로그램, 비기는 경우는 없다

입력 :
A, B가 무엇을 냈는지 빈칸을 기준으로 주어짐.
A, B 중 이긴 사람 출력.
'''

a, b = map(int, input().split())

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
elif a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')

'''
다른 풀이 1
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
else:
    print('A')
'''