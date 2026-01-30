a=input("enter value")
n=str(a)
r=0
for i in a:
    r=a[::-1]
if r==n:
    print("Palindrome")
else:
    print("Not Palindrome")