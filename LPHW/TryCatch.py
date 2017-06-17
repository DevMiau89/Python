
try:
    a = range(1,7)
    print a[8]    
except IndexError as e:
    print(e)
except Exception as e:
    print(e)    
else: 
    print a
    print "This line will always be executed"       