#12. Write a Python program to write a list to a file.
def write_list(fname, a_list):
    with open(fname, "r+") as f:
        for c in a_list:
            f.write("{}\n".format(c))
    content = open(fname) 
    z = content.read()
    return z

print write_list("C:\ex15_sample.txt", ["kot", "puch"])

