carNum=input("")
if carNum[0].isalpha and carNum[0].isupper and carNum[1].isalpha and carNum[1].isupper and carNum[2].isdigit and carNum[3].isdigit and carNum[2].isdigit and carNum[4].isalpha and carNum[4].isupper :
    condition=True
else:
    condition=False
if condition:
    print("Valid")
else:
    print("Invalid")