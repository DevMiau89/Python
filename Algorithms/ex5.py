#5. Write a Python program to sort a list of elements using the selection sort algorithm.

sample_Data = [14,46,43,27,57,41,45,21,70]

for k in range(0,len(sample_Data) -1):
    minIndex = k
    for i in range(k+1,len(sample_Data)):
        if sample_Data[i] < sample_Data[minIndex]:
            minIndex = i
    if minIndex != k:
        sample_Data[k], sample_Data[minIndex] = sample_Data[minIndex], sample_Data[k]
         
print sample_Data
print "------------------"
#6. Write a Python program to sort a list of elements using the insertion sort algorithm.

lst = [14,46,43,27,57,41,45,21,70]
for i in range(1, len(lst)):
    for j in range(i - 1, -1, -1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        else:
            break
print lst            