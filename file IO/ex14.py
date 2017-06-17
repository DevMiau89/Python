#16. Write a Python program to assess if a file is closed or not.

with open('C:\ex15_sample.txt') as f:
    f.close()
    if f.closed:
        print True
    else:
        print False
    
#17. Write a Python program to remove newline characters from a file. 

with open('C:\ex15_sample.txt') as f:
    
