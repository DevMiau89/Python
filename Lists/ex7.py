#34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. 

def computing_primes(number):
    non_prime_nums = []
    prime_nums = []
    lenght = range(2, number+1)   
    for i in lenght:      
        if i not in non_prime_nums:
            prime_nums.append(i) 
            for j in range(i*i, number+1, i):
                non_prime_nums.append(j)    
    return prime_nums

# func call
print computing_primes(40)


#35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

def concatenating_list(sample_list, n):
    lenght = range(1, n+1)
    for j in lenght:
        for i in sample_list:
            add =  i + str(j)
            print add
              
    

print concatenating_list(["p", "q"], 5)

#36. Write a Python program to get variable unique identification number or string.

x = 10
print id
print format(id(x), 'x')
s = 'w3resource'  
print(format(id(s), 'x'))

