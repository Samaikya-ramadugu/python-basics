n=int(input("Enter a number "))
count=0
if n<2:
    count=1
else:
    for i in range(2,(n/2)+1):
        if n%i==0:
         count=1
         break
if count==1:
    print("Not a Prime")
else:
    print("prime")