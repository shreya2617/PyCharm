sp=int(input("enter selling price"))
cp=int(input("enter cost price"))
p=sp-cp
l=cp-sp
if p>l:
    print("its profit")
else:
    print("its loss")