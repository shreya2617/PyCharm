n=int(input("enter any number"))
i=2
while i<=n:
    print(i)
    i=i+2
    print()
#or

n=int(input("enter any number"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1