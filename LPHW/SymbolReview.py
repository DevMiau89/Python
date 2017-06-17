aList = [0, 1, 2, 3, 4, 5]
del aList[5]

print aList

def list_check():
    i = int(raw_input())
    j = 4
    if i in aList or j in aList:
        print "It has position %d and %d is in a list" % (i, j)
    else:
        print "Sorry, not in the list"    

list_check()

i = 0
j = 10

if i == 0 and j == 10:
    print "Good job!"
else:
    print "sorry. It didn't work"    
