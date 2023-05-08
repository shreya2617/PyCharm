n=int(input("enter any number"))
last=n%10
print(last)
while n>0:
    first=n%10
    n=n//10
    print(first+last)