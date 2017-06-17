#25. Write a Python program to locate the right insertion point for a specified value in sorted order.
import bisect
data =[5,4,2,3]
print bisect.bisect_right(data, 10)


#26. Write a Python program to insert items into a list in sorted order
import heapq
sample_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36] 

sorted_list = []

for i in sample_list:
    sorted_list.append(i)


print sorted(sample_list)

