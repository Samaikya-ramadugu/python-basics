n=int(input("Enter year"))
print("leap year"if(n%4==0 or (n%400==0 and n%100!=0)) else "not leap year")