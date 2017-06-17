#8. Write a python program to find the longest words
def file_read(fname):
    f = open(fname)
    my_text = []
    for i in range(len(fname)):
        my_text += f.readline()
        return max(my_text.split(),key = len)

print file_read("C:\ex15_sample.txt")


def file_reader(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()  
    max_len = len(max(words, key=len))  
    return [word for word in words if len(word) == max_len]  
  
print file_reader("C:\ex15_sample.txt")