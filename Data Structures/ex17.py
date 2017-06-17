#27. a Python program to create a queue and display all the members and size of the queue.
from Queue import *

q = Queue()

for i in range(4):
    q.put(i)

for i in list(q.queue):
    print i

print "Size of the queue is:"
print q.qsize()


#28. Write a Python program to find whether a queue is empty or not.

z = Queue()

print z.empty()
print q.empty()


