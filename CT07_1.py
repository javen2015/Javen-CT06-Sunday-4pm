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
# if name.isnumeric:#alphabets and numbers
#     print("True")
# else:
#     print("False")
password=input("What is your password?")
hasDigit=password.isdigit()
if password.isupper() and password.islower() and password.isdigit()==False and password.isalpha()==False and password.isalnum() and len(password)>7:
    print("True")
else:
    print("False")


# len(list)

