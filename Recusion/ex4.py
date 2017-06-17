#5. Write a Python program to solve the Fibonacci sequence using recursion.
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1  
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print (Fibonacci(4))     

  