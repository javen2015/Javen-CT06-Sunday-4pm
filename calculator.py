num1= int(input())
num2=int(input())
operator=input("m,dr,d,p,mi")
if operator == "p":
    print(num1 + num2)
if operator == "mi":
    print(num1 - num2)
if operator == "m":
    print(num1 * num2)
if operator == "d":
    print(num1 // num2)
if operator == "dr":
    print(num1 / num2)