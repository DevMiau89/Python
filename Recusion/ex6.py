#7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
    x = 2
    if n <= 0:
        return 0
    else:
        return n + sum_series(n - x)
        x += 2

print sum_series(10)        

#8. Write a Python program to calculate the harmonic sum of n-1.
def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1/n + harmonic_sum(float(n - 1))


print harmonic_sum(4)



