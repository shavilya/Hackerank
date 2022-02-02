import numpy as np 

a = int(input())

arr_A = np.array([input().split(' ') for _ in range(a)] , int) 
arr_B = np.array([input().split(' ') for _ in range(a)] , int) 

print(np.dot(arr_A,arr_B))

