a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

z=[]

for i in a:
    if i <= 5:
        print "Adding element %d to the list" % i
        z.append(i)

print z        
  
print "Please enter the number: "
num = int(raw_input("> ")) 

x = [i for i in a if i < num]
c = []

for y in x:    
    c.append(y)

print c    