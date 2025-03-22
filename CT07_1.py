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
# if name.isalnum:#alphabets and numbers
#     print("True")
# else:
#     print("False")
# hasDigit=password.isdigit()
# if password.isupper()==False and password.islower() and password.isdigit()==False and password.isalpha()==False and password.isnumeric()==False and len(password)>7:
#     print("True")
# else:
#     print("False")


# len(list)




# password=input("What is your password?")
# hasUpper=not(password.islower())
# hasLower=not(password.isupper())
# hasNum=not(password.isalpha())

# if password.isalnum() and len(password)>7 and hasUpper and hasLower and hasNum:
#     print("True")
# else:
#     print("False")


# output=""
# name=input()
# case=True
# for char in name:
#     if case:
#         output+=char.upper()
#         case=False
#     else:
#         output+=char.lower()
#         case=True
# print(output)

# print("BruhBruh"[3:1:-1])

# sentence="Hello World"
# splitsentence=sentence.split(" ")
# reversedsentence=splitsentence[0][::-1]
# reversedsentence+=" "
# reversedsentence+=splitsentence[1][::-1]
# print(reversedsentence)








# while True:
#     ui=input()
#     if ui == "end":
#         break
#     reversedui=str(ui)[::-1]  
#     output=reversedui==str(ui)
#     print(output) 
# counter=0
# output=False
# ui=input()
# splitui=str(ui).split(" ")
# for i in range(len(splitui)):
#     reversedui=str(splitui[i])[::-1] 
#     print(reversedui)
#     if reversedui==str(splitui[i]):
#         counter+=1
# if counter==0:
#     print("False")
# else:
#     print("True "+str(counter))
# highestSellingFruit=[]
# sales_data=[
#     ["Apple",50,1.99],
#     ["Banana",40,0.99],
#     ["Orange",30,2.99],
#     ["Grapefruit",25,4.99],
#     ["Mange",20,3.99]
# ]
# fruit=""
# speech=""
# price=[]
# for i in range(len(sales_data)):
#     price.append(sales_data[i][2]+sales_data[i][1]*sales_data[i][2])
# if max(price)=="Apple":
#     speech+="1. Apple"+str(max(price))
#     fruit=0
# elif max(price)=="Banana":
#     speech+="1. Banana"+str(max(price))
#     fruit=1
# elif max(price)=="Orange":
#     speech+="1. Orange"+str(max(price))
#     fruit=2
# elif max(price)=="Grapefruit":
#     speech+="1. Grapefruit"+str(max(price))
#     fruit=3
# else:
#     speech+="1. Mango"+str(max(price))
#     fruit=4
# highestSellingFruit.append("1. "+str(sales_data[fruit]))
# sales_data.pop(fruit)
# if max(price)=="Apple":
#     speech+="1. Apple"+str(max(price))
#     fruit=0
# elif max(price)=="Banana":
#     speech+="1. Banana"+str(max(price))
#     fruit=1
# elif max(price)=="Orange":
#     speech+="1. Orange"+str(max(price))
#     fruit=2
# elif max(price)=="Grapefruit":
#     speech+="1. Grapefruit"+str(max(price))
#     fruit=3
# else:
#     speech+="1. Mango"+str(max(price))
#     fruit=4
# highestSellingFruit.append("2. "+str(sales_data[fruit]))
# sales_data.pop(fruit)
# if max(price)=="Apple":
#     speech+="1. Apple"+str(max(price))
#     fruit=0
# elif max(price)=="Banana":
#     speech+="1. Banana"+str(max(price))
#     fruit=1
# elif max(price)=="Orange":
#     speech+="1. Orange"+str(max(price))
#     fruit=2
# elif max(price)=="Grapefruit":
#     speech+="1. Grapefruit"+str(max(price))
#     fruit=3
# else:
#     speech+="1. Mango"+str(max(price))
#     fruit=4
# highestSellingFruit.append("3. "+str(sales_data[fruit]))
# sales_data.pop(fruit)
# print(highestSellingFruit[0])
# print(highestSellingFruit[1])
# print(highestSellingFruit[2])


# sales_data=["Apple",50,1.99],
# ["Banana",40,0.99],
# ["Orange",30,2.99],
# ["Grapefruit",25,4.99],
# ["Mange",20,3.99]
# price=[]
# top3=[]

# for item in sales_data:
#     price.append(item[1]*item[2])
# for i in range(3):
#     highest=max(price)
#     index_of_highest=price.index(highest)
#     top3.append(index_of_highest)
#     price[index_of_highest]
# print("Top 1 fruit: " + str(sales_data[top3[0]][1]))
# print("Top 2 fruit: " + str(sales_data[top3[1]][1]))
# print("Top 3 fruit: " + str(sales_data[top3[2]][1]))

def a():
        n=input("Username")
        p=input("Password")
        w=input("Website")
        passwordlist.append(n)
        passwordlist.append(p)
        passwordlist.append(w)
        fullPasswordList.append(passwordlist)
        print(fullPasswordList)
fullPasswordList=[]
passwordlist=[]
while True:
    ui=input("Enter a s d or q")
    a()