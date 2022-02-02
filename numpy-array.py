import numpy

def arrays(arr):
    rev_list = arr.reverse()  
    list1 = numpy.array(arr,float)
    return list1 
arr = input().strip().split(' ')
result = arrays(arr)
print(result)