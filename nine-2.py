low,high=2,20
primes=[2]
for i in range(low,high+1):
    count=0
    if i<2:
        count=1
        break
    if i%2==0:
        continue
    n=2
    while n<int(i/2):
        if i%n==0:
            count=1
            break
        n+=1
    if count==0:
        primes.append(i)
print(primes)
        