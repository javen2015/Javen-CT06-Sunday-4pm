import random
numberRange=input("What is the number range? Type the minimum number and the maximum number seperated by a space.")
splitNumberRange=numberRange.split(" ")
number=random.randint(int(splitNumberRange[0]),int(splitNumberRange[1]))

print(number)