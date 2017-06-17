#3. Write a Python program of recursion list sum.
Test_Data = [4, 2, [3,1,[9,12,[14,5]]], [7,1]]

def fact_sum(a_list):
    x = 0
    for i in a_list:
        if isinstance(i, list):
            print "i is a list:", i
            x = x + fact_sum(i) 
            #print "*",fact_sum(i)
        else:
            print "i is: ",i
            x = x + i
    return x        

z = fact_sum(Test_Data)

print z