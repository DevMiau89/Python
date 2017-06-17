#22. Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time. 
from heapq import *

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heap = []

for value in l:
    heappush(heap, value)

z = [heappop(heap) for i in range(len(heap))]

print z

#23. Write a Python program to get the two largest and three smallest items from a dataset.
import heapq
h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]

print heapq.nlargest(2, h)
print heapq.nsmallest(3, h)
