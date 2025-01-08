# 알고리즘:
# 시간복잡도: 약 O(N)
# 자료구조: 큐
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck_list = deque(truck_weights)
    now_weight = time = 0
    
    while truck_list:
        if bridge and time - bridge[0][1] == bridge_length:
            now_weight -= bridge[0][0]
            bridge.popleft()
            
        if len(bridge) < bridge_length and (now_weight + truck_list[0]) <= weight:
            waiting_truck = truck_list.popleft()
            bridge.append((waiting_truck, time))
            now_weight += waiting_truck
        
        time += 1
    return time + bridge_length