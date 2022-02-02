if __name__ =='__main__':
    set_a = set(map(int,input().split(' ')))
    no_of_other_sets = int(input())
    set_b , set_c = (set(map(int,input().split(' '))), set(map(int,input().split(' '))))

    if set_a.issuperset(set_b):
        if set_a.issuperset(set_c):
            print('True')
        else :
            print('False')
    else : 
        print('False')
