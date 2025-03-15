# list=[1,10,9,8,7,20,16]
# print(sorted(list))
# print(list[1:3]) #list[start(inclusive):end(exclusive(-1))]


# name=input("What is your name?")
# if name.isalpha:#alphabet
#     print("True")
# else:
#     print("False")
# if name.isnumeric:#numbers
#     print("True")
# else:
#     print("False")
password=input("What is your password?")
hasUpper=password.isupper()
hasLower=password.islower()
hasDigit=password.isdigit()
print()
if password.isalnum() and len(password)>7 and hasUpper and hasLower and hasDigit:#alphabets and numbers
    print("True")
else:
    print("False")


# len(list)

