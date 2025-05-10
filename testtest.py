carNum=input("")
condition=0
if carNum[0].isalpha and carNum[0].isupper:
    condition=True

if condition:
    print("Valid")
else:
    print("Invalid")