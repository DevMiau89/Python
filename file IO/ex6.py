#6. Write a Python program to read a file line by line store it into a variable. 
def read_lines(fname):
    with open(fname, "r") as f:
        f_store = f.readlines()
        return f_store

print read_lines("C:\ex15_sample.txt")    

print "-------------------"

#7. Write a Python program to read a file line by line store it into an array. 

def array_store(foo):   
    with open(foo) as f:
        my_array = [] 
        for line in f:
            my_array.append(line)
        print my_array

array_store("C:\ex15_sample.txt")            

def file_read(fname):  
        content_array = []  
        with open(fname) as f:  
                #Content_list is the list that contains the read lines.       
                for line in f:  
                        content_array.append(line)  
                print(content_array)
                  
print "**********"  
file_read("C:\ex15_sample.txt") 