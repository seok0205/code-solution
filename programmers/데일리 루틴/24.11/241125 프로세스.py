'''
운영체제가 아래 규칙에 따라 프로세스를 관리함.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

실행 대기 큐에 있는 프로세스의 중요도의 배열 priorities,
몇 번째로 실행되는지 알고 싶은 프로세스의 위치를 알려주는 location.
특정 프로세스가 몇번째로 실행되는지 반환.

제한 사항 :
1 <= len(priorities) <= 100
1 <= priorities[i] <= 9
priorities[i]는 우선순위 나타내고 클수록 우선순위 높음.

location은 0 이상 (대기 큐의 프로세스 수 - 1) 이하의 값.
priorities[0]은 0, 두 번째는 1... 과 같이 표현.

접근 :
1. 가장 중요도 높은 프로세스 찾음.
2. 실행한 프로세스 0으로 바꾸면서 다음 최대값 찾음.
3. 이 과정 중 만약 location과 인덱스가 일치한다면 반복문 탈출.
'''

priorities = [2, 1, 3, 2]
location = 2

result = 0  # 실행 순서(답)
first = priorities.index(max(priorities)) # 중요도 가장 높은 프로세스 탐색.

while True:
    n = max(priorities) # 중요도 큰 프로세스 값

    if priorities[first] == n:  # 현재 실행 순서의 프로세스 중요도가 가장 큰 중요도라면
        priorities[first] = 0   # 중요도를 0으로 바꾸고
        result += 1 # 실행 순서를 1 증가.

        if first == location:   # 실행시킨 프로세스와 location이 동일 시
            break   # 반복문 종료.

    first += 1  # 다음 순서
    if first >= len(priorities):    # 프로세스의 순서가 끝까지 갔을 때
        first = 0   # 맨 앞으로 순서를 옮김.

print(result)