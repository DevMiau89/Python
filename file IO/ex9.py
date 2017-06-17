#10. Write a Python program to count the frequency of words in a file.
from collections import defaultdict

def word_frequency(fname):
    with open(fname) as f:
        d = defaultdict(int)
        for word in f.read().split():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        return d
       
print word_frequency("C:\case_test.txt")

