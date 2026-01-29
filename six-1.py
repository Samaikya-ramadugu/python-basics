#leap year or not

n=int(input("Enter year"))
if (n%400==0) or (n%4==0 and n%100!=0):
    print(n,"is a leap year")
else:
    print(n,"isn't a leap year")