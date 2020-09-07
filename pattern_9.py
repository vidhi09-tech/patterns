for i in range(0,3):
    for j in range(0,5):
        if((i+j)/2==1 or (i+j)%2==0):
            if((i+j)==4 or i==0 and j==0):
                print(" ",end='')
            else:
                print("#",end='')
        else:
            print(" ",end='')
    print()
