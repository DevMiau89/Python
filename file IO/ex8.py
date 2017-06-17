#9. Write a Python program to count the number of lines in a text file.
def line_counter(fname):
    with open(fname) as f:
        lines = len(f.readlines())
    return lines

print line_counter("C:\ex15_sample.txt")

def file_lengthy(fname):  
        with open(fname) as f:  
                for i, l in enumerate(f):  
                        pass  
        return i + 1  

print("Number of lines in the file: ",file_lengthy("C:\ex15_sample.txt")) 




