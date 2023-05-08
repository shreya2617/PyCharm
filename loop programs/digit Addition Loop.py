a=int(input("enter any number"))
sum=0
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
print("addition is:",sum)