    
number_list = []
while True:
    number = float(raw_input("Please enter a number: "))
    if number != 0:
        number_list.append(number)
    else:
        break    

z = reduce(lambda x, y: x + y, number_list) / len(number_list)  

print "Your average is:", z

suma = 0

for element in number_list:
    suma += element

avg = suma / len(number_list)

print "Sum = ", suma
print "Avg = ", avg