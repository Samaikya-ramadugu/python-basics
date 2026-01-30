#palindrome or not
n=int(input("Enter a number "))
temp=n
r=0
while n>0:
    num=n%10
    r=r*10+num
    n=n//10
if r==temp:
    print("Palindrome")
else:
    print("Not a palindrome")
