for i in range(1,9):
    for j in range(1,6):
        if(i==4 or i==8 or j==1 and i!=1 and i!=2 or j==5 and i!=1 and i!=2
                or i==2 and j==2 or i==2 and j==4 or i==1 and j==3):
            print("#",end='')
        else:
            print(" ",end='')
    print()