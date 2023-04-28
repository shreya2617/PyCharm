a=int(input("enter first number"))
b=int(input("enter second number"))
print(a,b)
c=a
a=b
b=c
print(a,b)

#without using third variable
a=int(input("enter first number"))
b=int(input("enter second number"))
print("value of a",a)
print("value of b",b)
a=a+b
b=a-b
a=a-b
print("value of a",a)
print("value of b",b)