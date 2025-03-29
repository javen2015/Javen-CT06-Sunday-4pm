import random
numberRange=input("What is the number range? Type the minimum number and the maximum number seperated by a space.")
splitNumberRange=numberRange.split(" ")
number=random.randint(int(splitNumberRange[0]),int(splitNumberRange[1]))
minusing=int(int(splitNumberRange[1])+1)-int(splitNumberRange[0])
dividingNumber=100/minusing
rounded=round(dividingNumber),2
print("There is a "+str(rounded)+"% chance of each number generating.")
print(number)