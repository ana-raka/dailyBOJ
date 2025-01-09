# 알고리즘: 우선순위 큐
# 시간복잡도: O(NlogN)
# 자료구조: 우선순위 큐
from queue import PriorityQueue

def solution(jobs):
    jobs.sort(key=lambda x: x[0]) 
    pque = PriorityQueue()
    
    current_time = 0
    total_time = 0
    job_index = 0
    job_count = len(jobs)
    
    while job_index < job_count or not pque.empty():
        while job_index < job_count and jobs[job_index][0] <= current_time:
            req_time, spend_time = jobs[job_index]
            pque.put((spend_time, req_time))
            job_index += 1
        
        if not pque.empty():
            spend_time, req_time = pque.get()
            current_time += spend_time
            total_time += (current_time - req_time) 
        else:
            current_time = jobs[job_index][0]
    
    return total_time // job_count