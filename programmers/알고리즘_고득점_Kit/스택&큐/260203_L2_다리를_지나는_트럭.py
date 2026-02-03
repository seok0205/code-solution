'''
L2 다리를 지나는 트럭

문제 설명:
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성

제약:
bridge_length는 1 이상 10,000 이하
weight는 1 이상 10,000 이하
truck_weights의 길이는 1 이상 10,000 이하
모든 트럭의 무게는 1 이상 weight 이하
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    idx = 0
    cnt = 0
    cw = 0
    
    while True:
        if cnt == len(truck_weights):
            return time
        
        time += 1
        n = bridge.popleft()
        if n:
            cw -= n
            cnt += 1
            
        if idx < len(truck_weights) and cw + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            cw += truck_weights[idx]
            idx += 1
        else:
            bridge.append(0)
        
        