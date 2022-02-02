"""import re 
str1 = input()

vowel_patter = re.compile(r'[aeiouAEIOU]{2,}')

if re.search(r'[aeiouAEIOU]{2,}',str1):
    regex = vowel_patter.findall(str1)
    for i in regex : 
        print(i)
else : 
    print(-1)
"""

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))