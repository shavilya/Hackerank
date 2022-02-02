"""no_of_plants  = int(input())
height_of_plants = set(input().split(' '))
sum_of_heights = 0 
len_of_plants = 0 
for i in height_of_plants:
    sum_of_heights+=int(i)
    len_of_plants+=1 


mickey_takes_average  = sum_of_heights / len_of_plants 
print("{:.3f}".format(mickey_takes_average))"""

no_of_plants  = int(input())
height_of_plants = set(input().split(' '))

mapped_plants = map(int,height_of_plants)
sum_of_height_of_plants = sum(mapped_plants)
mickey_takes_average = sum_of_height_of_plants/len(height_of_plants)

print(mickey_takes_average)