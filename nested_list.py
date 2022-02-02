if __name__ == '__main__':
    final_name_score = [ ]

    n=int(input())
    arr=[[input(),float(input())] for _ in range(0,n)]
    arr.sort(key=lambda x: (x[1],x[0]))
    name = [i[0] for i in arr]
    score = [i[1] for i in arr]
    
    min_val=min(score)
    while score[0]==min_val:
        score.remove(score[0])
        name.remove(name[0])    
    for x in range(0,len(score)):
        if score[x]==min(score):
            print(name[x])