def collatz(x,result): #returns number of passes to get to 1
    if x==1: return result+1
    if x%2==0: return collatz(x/2,result+1)
    return collatz(3*x+1,result+1)

max=0
startmax=0
for x in range(1,1000000):
    c=collatz(x,0)
    if max<c:
        max=c
        startmax=x

print(startmax)