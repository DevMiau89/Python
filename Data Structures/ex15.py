#24. Write a Python program to locate the left insertion point for a specified value in sorted order
import bisect
data =[5,4,2,3]
print bisect.bisect_left(data, 10)


def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
    
a = [1,2,4,5]
print(index(a, 0))
print(index(a, 3))

