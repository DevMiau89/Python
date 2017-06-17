#13. Write a Python program to copy the contents of a file to another file .
import shutil

shutil.copyfile("C:\ex15_sample.txt", "C:\case_test.txt")

with open("C:\case_test.txt", "r") as f:
    print f.read()

f.close()
print "======================="

#14. Write a Python program to combine each line from first file with the corresponding line in second file. 

with open("C:\ex15_sample.txt", "r+") as f1:
    with open("C:\case_test.txt", "r+") as f2:
        for line1,line2 in zip(f1, f2):
            print line1 + line2




