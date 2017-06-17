#17. Write a Python program to remove newline characters from a file.

with open('C:\ex15_sample.txt', 'r') as f:
    my_file = f.readlines()
    d = [s.replace('\n', '') for s in my_file]
    print d