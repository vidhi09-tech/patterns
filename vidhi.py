for i in range(1,6):
    for j in range(1,19):
        if(j==10 or j==11 or j==14 or j==17 or j==18 or i==3 and j==13 or i==3 and j==15 or i==3 and j==16 or i==3 and j==16
        or i==3 and j==7 or i==3 and j==3 or i==2 and j==12 or i==2 and j==8 or i==2 and j==2 or i==4 and j==12 or i==4
        and j==4 or i==4 and j==6 or i==1 and j==1 or i==1 and j==9 or i==5 and j==5):
            print("#",end=' ')
        else:
            print(" ",end=' ')
    print()