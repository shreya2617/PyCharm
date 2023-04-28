bs=int(input("enter basic salary"))
if bs<=10000:
    hra=bs*0.2
    da=bs*0.8
    total=bs+da+hra
    print("Total salary is:",total)
elif bs<=20000:
    hra=bs*0.25
    da=bs*0.9
    total=bs+da+hra
    print("Total salary is:",total)
else:
    hra=bs*0.3
    da=bs*0.9
    total=hra+da
    print("Total salary is:",total)