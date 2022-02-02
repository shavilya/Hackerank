if __name__ == '__main__':
    (_, set_A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, set_B) = (input().split()[0],set(map(int, input().split())))
        getattr(set_A, command)(set_B)

    print (sum(set_A))