import sys
from queue import PriorityQueue

input = sys.stdin.readline

pq = PriorityQueue()
for i in range(int(input().rstrip())):
    pq.put(int(input().rstrip()))
res = 0
if pq.qsize() == 1:
    print(0)
    exit()
while True:
    first_deck = pq.get()
    second_deck = pq.get()
    new_deck = first_deck + second_deck
    res += new_deck
    if pq.qsize() == 0:
        print(res)
        exit()
    pq.put(new_deck)