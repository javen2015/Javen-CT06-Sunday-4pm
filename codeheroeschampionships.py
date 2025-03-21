sum=0
n=int(input("What is n?"))
x=int(input("What is x?"))
for i in range(x):
    for r in range(n):
        sum=sum+(r+1*n)
print(sum)