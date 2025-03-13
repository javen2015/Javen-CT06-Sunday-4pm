num=1
foods=[]
numoffood=int(input("How many foods are there in the menu?"))
for i in range(numoffood):
    food=input("Who is student #"+str(i+1)+" ?")
    foods.append(food)
for i in food:
    print(str(num),".",str(i))
    num+=1