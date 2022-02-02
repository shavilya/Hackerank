import numpy as np
from numpy.core.fromnumeric import prod 

n,m = map(int,input().split(' '))
data = np.array([input().split(' ') for _ in range(n)],int)

sum_data = np.sum(data ,axis = 0)
print(prod(sum_data))