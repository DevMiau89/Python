#4. Write a Python program to read last n lines of a file.
def last_line(foo, n):
    f = open(foo)
    my_lines = ''
    for i in range(len(foo)):
        my_lines += (f.readline())
    return my_lines.split("\n")[-n:]
    
print last_line("C:\case_test.txt", 3)