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
        front_truck = truck_list[0]
        if len(bridge) < bridge_length and (now_weight + front_truck) <= weight:
            bridge.append((truck_list[0], time))
            now_weight += truck_list[0]
            truck_list.popleft()
            
        time += 1
    return time + bridge_length