triangles=[1,3,6,10,15,21]

def factor(x):
    result=[]
    for i in range(1,int(x**0.5+1)):
        if x % i==0:
            result.append(i)
            result.append(x/i)
    return len(result)

while factor(triangles[len(triangles)-1])<=500:
    triangles.append(triangles[len(triangles)-1]+len(triangles)+1)
    print(triangles[len(triangles)-1])

print(triangles[len(triangles)-1])