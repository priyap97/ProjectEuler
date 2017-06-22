sumofsquares=0
squareofsums=0
for x in range(1,101):
    sumofsquares+=(x*x)
for y in range(1,101):
    squareofsums+=y
squareofsums*=squareofsums
print(squareofsums-sumofsquares)