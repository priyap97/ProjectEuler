string=''
rev=''
x=0
y=0
p=0
for num1 in range (100,1000):
    for num2 in range (100,1000):
        string=str(num1*num2)
        rev=''.join(reversed(string))
        if string == rev:
            if(p<num1*num2) : p=num1*num2
print(p)
