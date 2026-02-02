'''
기능 개선 작업 수행 중. 각 기능은 진도가 100퍼센트일 때 서비스에 반영 가능.
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses,
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어짐.
각 배포마다 몇 개의 기능이 배포되는지를 return 하는 문제.

제한 사항 :
작업 개수는 100개 이하.
작업 진도는 100 미만 자연수.
작업 속도는 100 이하 자연수.
배포는 하루에 한번만 가능, 하루 끝에 이루어짐. 예로, 진도율이 95퍼센트인 작업의 개발 속도가 4퍼센트면 배포는 2일 뒤 이뤄짐.

접근 :
1. progresses 배열에서 100이 되면 리스트에서 없애는 형식으로 다가감.
2. 배열의 맨 앞 요소가 100이 되는 순간 연속해서 100인 기능은 배포.
3. while문에서 cnt라는 배포된 기능 개수를 담은 변수 활용해 if문으로 배포가 되어야만 0이 자연수로 바뀌면서 result에 cnt가 추가됨.
4. 하루 progresses의 진도가 speeds이고, 각 배열의 인덱스는 같은 기능을 가리키므로, for문으로 progresses[i], speeds[i]를 더해서 다음 날의 배열 만듦.
5. 위과정 반복함.
'''

def solution(progresses, speeds):
    result = []
    cnt = 0
    while progresses:
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        if cnt:
            result.append(cnt)
            cnt = 0
        
    return result