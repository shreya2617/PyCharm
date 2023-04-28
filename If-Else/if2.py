x=int(input("enter any number"))
if x%5==0 and x%11==0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")



a1=int(input("enter first angle"))
a2=int(input('enter second angel'))
a3=int(input("enter third ange"))
sum=a1+a2+a3
if sum==180:
    print("triangle is valid")
else:
    print('triangle is invalid')