#21. Write a Python program to push an item on the heap, then pop and return the smallest item from the heap. 
from heapq import *

a_list = [('V', 1), ('V', 3) ,('V', 2)]

heap = []

for i in a_list:
    heappush(heap, i)

print heap
print heappushpop(heap, ('V', 6))

print "------------------"
for a in heap:
    print a     