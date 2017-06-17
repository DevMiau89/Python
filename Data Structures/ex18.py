#29. Write a Python program to create a FIFO queue.
from Queue import *

q = LifoQueue()

for i in range(5):
    q.put(i)

for i in q.queue:
    print i

print "----------------------"

#30. Write a Python program to create a LIFO queue. 
z = Queue()    

for n in range(3):
    z.put(i)

for i in list(q.queue):
    print q.get()