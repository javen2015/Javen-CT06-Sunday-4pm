carNum = input("")

# Initialize condition as False
condition = False

# Check if length is 6 or 7
if len(carNum) == 6 or len(carNum) == 7:
    # Check first 2 characters are uppercase letters
    if carNum[0].isupper() and carNum[1].isupper():
        # Check middle part (3 or 4 digits)
        if carNum[2].isdigit() and carNum[3].isdigit() and (carNum[4].isdigit() or len(carNum) == 6):
            # Check last character is an uppercase letter
            if carNum[-1].isupper():
                condition = True

# Output based on the condition
if condition:
    print("Valid")
else:
    print("Invalid")
