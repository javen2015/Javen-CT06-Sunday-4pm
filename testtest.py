carNum=input("")
condition=0
if carNum[0].isalpha and carNum[0].isupper and carNum[1].isalpha and carNum[1].isupper and carNum[2].isdigit and carNum[2].isdigit :
    condition=True

if condition:
    print("Valid")
else:
    print("Invalid")