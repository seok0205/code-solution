#n개의 구역의 벽에 m미터의 롤러로 덧칠하려고한다. (벽은의 너비는 1m)
#주어진 section의 벽에 최소 몇번 롤러질을 해야 덧칠을 끝낼 수 있는지 구하는 문제.

n = 8
m = 4
section = [1, 4, 5, 8]

def solution(n, m, section):
    result = 0
    complete = 0    #한번 칠했을 때, 커버할 수 있는 최대 구역.
    for i in section:   #칠해야할 벽 모두 탐색.
        if i>complete:  #한번 칠했을때 완료한 구역보다 클때만.
            complete = i+m-1    #예를 들어 1구역과 4구역을 한꺼번에 칠했다. 그럼 4구역을다시 칠하는건 손해. 5구역부터 칠하는 게 이득.
            result += 1
    return result
    
print(solution(n,m,section))