for i in range(1,5):
    for j in range(1,5):
        if i==4 or j==4 or (i==3 and j==3)or (i==2 and j==3) or (i==3 or j==2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()