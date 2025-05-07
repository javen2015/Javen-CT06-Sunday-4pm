mapping = ["A","Z","Y","X","U","T","S","R","P","M","L","K","J","H","G","E","D","C","B"]
userCarPlate=input("")
carPlate=[]
carPlate.append(ord(userCarPlate[1])-64)
carPlate.append(ord(userCarPlate[2])-64)
carPlate.append(userCarPlate[3])
carPlate.append(userCarPlate[4])
carPlate.append(userCarPlate[5])
carPlate.append(userCarPlate[6])
numberList=[]
numberList.append(int(carPlate[0])*9)
numberList.append(int(carPlate[1])*4)
numberList.append(int(carPlate[2])*5)
numberList.append(int(carPlate[3])*4)
numberList.append(int(carPlate[4])*3)
numberList.append(int(carPlate[5])*2)
sum=numberList[0]+numberList[1]+numberList[2]+numberList[3]+numberList[4]+numberList[5]
remainder=sum%19
if(mapping[remainder] == userCarPlate[7]):
    print("Valid")
else:
    print("Invalid")