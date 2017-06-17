#19. Write a Python program to push three items into the heap and print the items from the heap. 
from heapq import heappush
heap = []
heappush(heap, ('V', 1))
heappush(heap, ('V', 2))
heappush(heap, ('V', 3))

for i in heap:
    print i

my_list = [1, 2, 3]

push_list = []

for item in my_list:
    heappush(push_list, item)

for i in push_list:
    print i

