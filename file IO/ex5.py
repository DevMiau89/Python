#5. Write a Python program to read a file line by line and store it into a list.
def file_read(fname):
    f = open(fname)
    z = f.readlines()
    return z

print file_read("C:\ex15_sample.txt")