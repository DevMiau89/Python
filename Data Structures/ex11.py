#18. Write a Python program to read a string and interpreting the string as an array of machine values.
from array import array
import binascii
array1 = array('i', [7, 8, 9, 10])
print('array1:', array1)

print('Bytes:', binascii.hexlify(array1))
array2 = array('i')
print('array2:', array2)

s = bin(int(binascii.hexlify('h'), 32))
print s