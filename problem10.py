primes=[2,3,5,7,11,13]
sum=2+3+5+7+11+13
num=17
while(num<2000000):
    isprime=True
    for x in primes:
        if x*x>num:
            break
        if num%x==0:
            isprime=False
            break
    if isprime:
        primes.append(num)
        sum+=num
    num+=2
print(sum)