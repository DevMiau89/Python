#20. Write a Python program to print alphabet pattern 'G'.

for i in range(0,7):
    if i == 0:
        print " " + "*" * 3
    elif i == 1:
        print "*" + (" " * 3) + "*"
    elif i == 3:
        print "* " + ("*" *3)    
    elif i == 4:
        print "*" + (" " * 3) + "*"
    elif i == 5:
        print "*" + (" " * 3) + "*"
    elif i == 6:
        print " "+ "*" * 3     
    else:
        print "*"

print "-------------------------"    

result_str=""    
for row in range(0,7):    
    for column in range(0,7):     
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)
       