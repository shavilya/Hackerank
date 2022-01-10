if __name__ == '__main__':
    n = int(input())
    number = [ ]
    for i in range(1,n+1):
        number.append(i)
    
    strings = [str(number) for number in number]
    a_string = "".join(strings)
    an_integer = int(a_string)
    
    print(an_integer)
   
