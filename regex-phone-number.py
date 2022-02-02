import re 


testcases = int(input())
regex = re.compile(r'^[7-9][0-9]{9}$')

for _ in range(testcases):
    if regex.findall(input()):
        print('YES')
    else : 
        print('NO')
