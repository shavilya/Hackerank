# Submitted with all 7 test cases passed.   
"""
if __name__ == '__main__':
    n = int(input().strip())
    
    odd_n = None 
    even_n = None
    if n % 2 == 0:
        even_n = n 
    else : 
        odd_n = n 
        
    
    if n == odd_n : 
        print('Weird')
    elif n == even_n and n > 2 and n < 5 : 
        print('Not Weird')
    elif n == even_n and n > 6 and n < 20 : 
        print('Weird')
    elif n == even_n and n > 20 : 
        print('Not Weird')
     
"""
        
# Submitted with all test cases passed.   

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
