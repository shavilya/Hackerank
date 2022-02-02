"""from itertools import combinations_with_replacement

string,number = input().split(' ')

output = list(sorted(combinations_with_replacement(string,int(number))))

for i in output : 
    string_string = "".join(i)
    print(string_string)    
"""

from itertools import combinations_with_replacement

s, k = input().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))