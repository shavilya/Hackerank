from itertools import permutations 

input_list = list(map(str,input().split(' ')))
string_input = input_list[0]
number_input = input_list[1]
output = list(sorted(permutations(string_input,int(number_input))))

for i in output : 
    other = "".join(i)
    print(other)

