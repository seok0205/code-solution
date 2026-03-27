'''
S5 10431 줄세우기

문제 설명:
새로 반에 배정받은 아이들에게 키 순서대로 번호를 부여함.
가장 작은아이가 1번, 가장 큰아이가 20번. 항상 20명임.
같은 키 가진 사람 한명도 없음.

아무나 한 명 뽑아서 줄의 맨 앞에 세움.
- 자기 앞에 자기보다 키 큰 학생 없으면 그냥 그자리에 섬.
- 자기 앞에 자기보다 큰 학생이 한명 이상 있다면, 그 중 가장 앞에 있는 학생의 바로 앞에 섬. 이때, A부터 그 뒤 모든 학생들은 한발짝 뒤로감.

이 과정 반복하면 오름차순으로 줄 설 수 있음.
아이들 키가 주어지고, 마지막 학생까지 수행할때, 학생들이 뒤로 몇번(한명당 한걸음 즉, 모든 과정에서의 발걸음 총합) 갈것인가?

입력:
첫줄 - P (1 <= P <= 1000) 테케 수
각 테스트케이스는 T와 20개의 양의 정수가 공백으로 주어짐.
20개의 정수는 아이들의 키이고, 밀리미터 단위로 나타낸것.
모든 테케는 독립적.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    data = list(map(int, input().split()))
    line = [data[1]]
    result = 0

    for i in range(2, 21):
        for j in range(i-1):
            if data[i] < line[j]:
                line.insert(j, data[i])
                result += (len(line) - j - 1)
                break
        else:
            line.append(data[i])
    
    print(data[0], result)