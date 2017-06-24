a=0
b=0
c=0
m=2
while c<950:
    for n in range(m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if c>950: break
        if a+b+c==1000: print(a*b*c)
    m+=1