n=int(input("Enter a number "))
count=0
if n<2:
    count=1
else:
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            count=1
            break
if count==1:
    print("Not a prime")
else:
    print("Prime")