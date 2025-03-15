'''
D3 13038 교환학생

연중무휴인 대학교가 존재
교환학생들을 위한 수업이 특정 요일에만 진행
정보는 7개의 정수로 표현

일월화수목금토 순서로 0혹은 1로 수업의 유무 알 수있음

수업이 어떠한 요일에도 열리지 않는 경우는 없다고 가정해도 됨
교환학생으로 n일동안 수업을 들으려고하면 목표를 위해 지내야하는 최소 일수 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    schedule = list(map(int, input().split()))
    
    cnt = schedule.count(1)
    
    for i in range(7):
        if schedule[i]:
            s = i
            break
    
    dif = N % cnt
    result = N // cnt * 7
    
    if dif:
        cnt = 0
        for i in range(s, 7):
            if schedule[i]:
                cnt += 1
            if dif == cnt:
                result += (i-s+1)
                break
    else:
        cnt = 7
        for i in range(6, -1, -1):
            if schedule[i]:
                cnt -= 1
                break
        
        result -= (cnt)
    
    print(f'#{tc} {result}')