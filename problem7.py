primes=[2,3,5,7,11,13]
num=17
while(len(primes)<10001):
    isprime=True
    for x in primes:
        if num%x==0:
            isprime=False
            break
    if isprime: primes.append(num)
    num+=2
print(primes[10000])