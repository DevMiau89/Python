#6. Write a Python program to get the sum of a non-negative integer.
def my_sum(n):
  my_num = str(n)
  counter = 0
  for i in my_num:
      counter += int(i)
  return counter    

print my_sum(345)      
print "----------------"

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(n / 10)
    
print sumDigits(345)    