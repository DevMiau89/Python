def foo():    
    for index in range(5):
        #index = index.next()
        print "\nindex is No %d" % index
        yield index

f = foo()

f.next()

my_nums = [x*x for x in [1,2,3,4,5]]

print my_nums

def square_numbers(nums):
     for i in xrange(5):
        yield i*i

x = square_numbers(5)
print x

for num in x:
    print num
