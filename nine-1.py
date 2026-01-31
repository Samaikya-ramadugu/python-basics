#checking prime or not in the given range
low,high=2,15
primes=[]

for i in range(low, high+1):
    count=0
    if i<2:
        continue
    if i==2:
        primes.append(2)
        continue
    for num in range(2,i):
        if i%num==0:
            count=1
            break
    if count==0:
        primes.append(i)
print(primes)


