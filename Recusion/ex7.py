#9. Write a Python program to calculate the geometric sum of n-1. 
def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (2**n) + geometric_sum(float(n - 1))

print geometric_sum(7)


#10. Write a Python program to calculate the value of 'a' to the power 'b'.
def power(n, r):
    if r == 0:
		return 1
    elif n == 0:
	    return 0
    elif r == 1:
		return n
    else:
        return n * pow(n, r-1)

print power(3, 4)   
