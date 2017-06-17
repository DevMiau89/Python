#2. Write a Python program to converting an Integer to a string in any base.
def to_string(n, base):
    conv_string = "0123456789ABCDEF"
    if n < base:
        return conv_string[n]
    else:
        return to_string(n/base, base) + conv_string[n%base]
print to_string(1453,16)
print "--------------------------------------"

#3. Write a Python program of recursion list sum.
Test_Data = [1, 2, [3,4], [5,6]]

def fact_sum(a_list):
    x = 0
    for i in a_list:
        if isinstance(i, list):
            x = x + fact_sum(i)
            print "-", x
            print "*",fact_sum(i)
        else:
            print "i is: ",i
            x = x + i
    return x        

fact_sum([1, 2, [3,4], [5,6]])