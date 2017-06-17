# I am opening a file

try:
    f = open("c:\Python\ex15_sample.txt", "r")
    print "Name of the file:", f.name

    for index in range(5):
        line = f.next()
        print "\nLine No %d - %s" % (index, line)    
except IOError as e:
    print(e)
except StopIteration as e:
    print(e)
except ValueError as e:
    print(e)
except Exception:
    "Sorry something went wrong"        
else: 
    f.close()    
finally:
    print "All done!"    


        