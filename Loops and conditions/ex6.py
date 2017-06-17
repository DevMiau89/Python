#9. Write a Python program to get the Fibonacci series between 0 to 50. 

x = 0
y = 1
for z in range(50):   
    z = x + y       
    print z
    x = y
    y = z
    

print "-----------------"

x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y

print "------------"

def fibR(n):
    if n==1 or n==2:
        return 1
    return fibR(n-1)+fibR(n-2)
print fibR(4)
