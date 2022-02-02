from itertools import product 

list_A = list(map(int,input().split(' ')))
list_B = list(map(int,input().split(' ')))

products = list(product(list_A,list_B))

for i in products : 
    print(i , sep = ' ' , end = ' ' , flush=True)


