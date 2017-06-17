a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = []

for i in a:   
    if i in b:
        a.remove(i)    
    else:
        c.append(i)

for x in b:
    c.append(x)        
          
c.sort()

print c




