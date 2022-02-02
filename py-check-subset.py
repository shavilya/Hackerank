if __name__ == '__main__':
    try : 
        no_of_testcases = int(input())

        while no_of_testcases > 0 : 
            no_of_element_a = int(input())
            set_a = set(map(int,input().split(' ')))
            no_of_element_b = int(input())
            set_b = set(map(int,input().split(' ')))

            if set_a.issubset(set_b):
                print('True')
            else : 
                print('False')

            no_of_testcases += 1 
    except EOFError as e  :
        e 

    