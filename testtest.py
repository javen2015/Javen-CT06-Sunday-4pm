carNum=input("")
condition=0
if carNum[0].isalpha and carNum[0].isupper:
    condition+=1

if condition:
    print("Valid")
else:
    print("Invalid")