#4. Write a Python program to sort a list of elements using the bubble sort algorithm.
sample_Data = [14,46,43,27,57,41,45,21,70]

for k in range(len(sample_Data)-1):
    flag = 0
    for i in range(len(sample_Data)-k-1):
        if sample_Data[i] > sample_Data[i + 1]:
            sample_Data[i], sample_Data[i + 1] = sample_Data[i+1], sample_Data[i]
            flag = 1

    if flag == 0:
        break           
print sample_Data
