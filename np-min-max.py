import numpy as np 

n,m = map(int,input().split(' '))
data = np.array([input().split(' ') for _ in range(n)], int)

min_data = np.min(data, axis = 1)
print(np.max(min_data))