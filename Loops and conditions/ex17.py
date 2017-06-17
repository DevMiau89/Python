#30. Write a Python program to print alphabet pattern 'Z'.

for i in range(0,7):
    if i == 0:
        print "*" * 8
    elif i == 1:
        print " "*6 + "*"
    elif i == 2:
        print " "*5 + "*" 
    elif i == 3:
        print " "*4 + "*" 
    elif i == 4:
        print " "*3 + "*" 
    elif i == 5:
        print " "*2 + "*"                     
    else:
        print "*" * 8    
