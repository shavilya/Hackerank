import numpy as np 
np.set_printoptions(sign=' ')
n,m = map(int,input().split(' '))
data = np.array([input().split(' ') for _ in range(n)], int)

print(np.mean(data,axis = 1))
print(np.var(data, axis = 0 ))
print("{:.11f}".format(np.std(data)))