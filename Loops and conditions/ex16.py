#25. Write a Python program to print alphabet pattern 'R'.
for i in range(0,7):
    if i == 0:
        print "*" * 4
    elif i == 1:
        print "*" + " "*4 + "*"
    elif i == 2:
        print "*" + " "*4 + "*"
    elif i == 3:
        print "*" * 4
    elif i == 4:
        print "*  *"    
    elif i == 5:
        print "*   *"    
    else:
        print "*    *"

print "------------------"
#27. Write a Python program to print alphabet pattern 'T'. 

for i in range(0,7):
    if i == 0:
        print "*" *7
    else:
        print "   *"   


print "------------------"         

#28. Write a Python program to print alphabet pattern 'U'.

for i in range(0,7):
    print "*      *"   
    if i == 6:
        print " "*2 + "*" * 4  