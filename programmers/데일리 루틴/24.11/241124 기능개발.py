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

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

result = []

while progresses:
    cnt = 0

    # 100이 되어 개발이 완료된 기술 배포.(이유는 progresses는 배포 우선순위가 인덱스 순서와 같으므로)
    while progresses and progresses[0] >= 100:  # 100이 아닌 기능이 나올때까지 인덱스가 0인 기능 pop.
        cnt += 1
        progresses.pop(0)
        speeds.pop(0)   # 기능도 같이 제거해야함. 아래 for문 때문.

    for i in range(len(progresses)):    # 바로 위의 배포를 나타내는 while문이 끝나면 progresses의 진도를 speeds를 통해 더함.
        progresses[i] += speeds[i]

    if cnt: # 만약 cnt가 증가했다면 cnt를 result에 추가. 변동없이 0이면 false로 인식해 if문 실행안함.
        result.append(cnt)

print(result)
