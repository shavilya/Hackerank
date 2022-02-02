import numpy as np 

n,m = map(int,input().split(' '))
elements = np.array([input().split(' ') for _ in range(n)], int)

print(np.transpose(elements))
print(elements.flatten())