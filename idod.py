carNum=input("")
condition=False
if len(carNum)==6:
    if carNum[0].isupper() and carNum[1].isupper():
        if carNum[2].isdigit() and carNum[3].isdigit() and carNum[4].isdigit():
            if carNum[5].isalpha():
                condition=True
if condition:
    