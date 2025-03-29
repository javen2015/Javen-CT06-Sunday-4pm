import random
numberRange=int(input("What is the number range? Type the minimum number and the maximum number seperated by a space."))
splitNumberRange=numberRange.split(" ")
number=random.randint(splitNumberRange[0],splitNumberRange[1])
print("There is a "+str(100/splitNumberRange[1])+"")
print(number)