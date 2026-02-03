'''
L2 프로세스

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
'''

def solution(priorities, location):
    length = len(priorities)
    idx = 0
    cnt = 0
    while True:
        if priorities[idx] == max(priorities[idx:idx+length]):
            cnt += 1
            length -= 1
            if idx == location:
                return cnt
        else:
            priorities.append(priorities[idx])
            if idx == location:
                location += length
        idx += 1