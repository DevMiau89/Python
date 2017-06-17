#7. Write a Python program to sort a list of elements using shell sort algorithm.

def shellSort(sample):
    lenght = len(sample)
    gap = lenght/2

    while gap >=1:
        i=gap
        while(i < lenght):
            value = sample[i]
            j=i
            while(j -gap >=0 and value < sample[j-gap]):
                sample[j] = sample[j - gap]
                j-=gap
                sample[j] = value
            i +=1
        gap /=2
print shellSort([3, 5, 9, 2, 4, 7])
