#22. Write a Python program to print alphabet pattern 'M'.

for i in range(0,7):
    if i == 2:
        print "*" + " " + "*" + " " + "*" + " *"
    elif i == 3:
        print "*" + 2* " "+ "*"+ " " + " *"
    else:
        print "*     *"        

print "---------------"
#23. Write a Python program to print alphabet pattern 'O'      

for i in range(0,7):
    if i == 0:
        print " " + ("*" * 3)
    elif i == 6:
        print " " + ("*" * 3)
    else:
        print "*   *"    
      
print "---------------"
#24. Write a Python program to print alphabet pattern 'P'

for i in range(0,7):
    if i == 0:
        print "*" * 4
    elif i == 1:
        print "*" + " "*4 + "*"
    elif i == 2:
        print "*" + " "*4 + "*"
    elif i == 3:
        print "*" * 4
    else:
        print "*"        