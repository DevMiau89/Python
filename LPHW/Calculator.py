
import math
calculate = ((4/3)* math.pi)**3 

print calculate


cover_book = 24.95
discount = 0.6
shipping_cost = 3
additional_copy = 0.75
amount_of_books = 60
currency = '$'

cost_1 = (cover_book * discount) * shipping_cost 
cost_2 = (cover_book * discount) * additional_copy * (amount_of_books - 1)
total_result = cost_1 + cost_2

print cost_1
print cost_2
print total_result


bookCost = 24.95
numBooks = 60.0

def cost(numBooks):
    bulkBookCost = ((bookCost * 0.60) * numBooks)
    shippingCost = (3.0 + (0.75 * (numBooks - 1)))
    totalCost = bulkBookCost + shippingCost
    print 'The total cost is: $', totalCost

cost(numBooks)

a = 10
a += 2

print a
 