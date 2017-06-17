#13. Write a Python function that prints out the first n rows of Pascal's triangle. 

list=[1]
for i in range(5):
    print(list)
    newlist=[]
    newlist.append(list[0])
    for i in range(len(list)-1):
        newlist.append(list[i]+list[i+1])
    newlist.append(list[-1])
    list=newlist

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]

pascal_triangle(6) 