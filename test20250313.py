# Write a PYTHON program that help students to determine 
# if they should go to school. You should prompt the user if 
# they have the following flu symptoms:

# Fever
# Cough
# Running nose
# Sore throat

# Your program should print

# “Please go and see a doctor” if the user has any of such symptoms; or
# “Please come into the class” if the user has no such symptoms.
# A user is deemed to be having a fever if the body temperature is above 38°C.

# You may assume that the user will type in either “yes” or “no” 
# for the subsequent questions.

# temperature=int(input("What is your temperature?"))
# cough=input("Do you have cough?")
# running_nose=input("Do you have a running nose?")
# sore_throat=input("Do you have a sore throat?")
# if temperature > 38:
#     print("Please go and see a doctor")
# elif cough == "yes":
#     print("Please go and see a doctor")
# elif running_nose=="yes":
#     print("Please go and see a doctor")
# elif sore_throat=="yes":
#     print("Please go and see a doctor")
# else:
#     print("Please come into the class")




##################################################################
# Taxis in Singapore run on a meter and charge the passenger 
# according to the distance travelled and the time spend waiting 
# in traffic jams or at traffic lights.

# The charges are as followed.

# Activity	Price
# Starting fare + 1km travelled	    $3.90
# Every subsequent 1km travelled	$0.25
# Every 1 minutes of waiting time	$0.33

# For example, if the user travelled for 14km and the amount of 
# waiting time is 5 minutes, then the fare calculation will be $8.80.

# Starting Fare + First km travelled: $3.90
# Subsequent 14 (- 1st km) km travelled: $0.25 × (14 - 1) = $3.25
# Waiting time of 5 minutes: $0.33 × 5 = $1.65
# Total fare: $3.90 + $3.25 + $1.65 = $8.80
# fare=0
# metresTravelled=int(input("How many metres have you travelled?"))
# waitingTime=int(input("How long have you waited?"))
# if metresTravelled > 0:
#     fare+=3.90
#     metresTravelled-=1
#     fare+=0.25*metresTravelled
# if waitingTime > 0:
#     fare+=0.33*waitingTime
# print("The total fare is $"+str(round(fare,2)))




####################################################################
# A hero goes on an adventure, starting at Full Health. 
# He has to fight monsters and clear obstacles in his adventure. 
# Sometimes, he takes damage while fighting these monsters.

# Write a PYTHON program that simulates the battles he fought 
# until his health reaches 0. Print out the number of battles 
# that he fought at the end of the program.

# Your hero must start with 100 health
# Print into the console "Hero starts on his adventure with Health: 100"

# Your hero loses between 1 to 15 health (randomly) each round.
# Update the console using "After fighting monsters, his Health is now: xx", 
# where "xx" is your hero's current Health

# Repeat until your hero's Health is less than or equals to 0
# Print "He fought xxx battles, and died", 
# where "xxx" is the number of rounds it took to reach 0 Health.

# import random
# heroHealth=100
# battles=0
# print("Hero starts on his adventure with Health: 100")
# while heroHealth > 0:
#     heroHealth-=random.randint(1,15)
#     print("After fighting monsters, his Health is now:"+str(heroHealth))
#     battles+=1
# print("He fought "+str(battles)+" battles, and died")


##################################################
# Write a PYTHON program that simulates a restaurant order system using list and while loop.

# Using a while loop to create a forever loop, 
# your program should ask the user "What would you like to order?", 
# store the user's response in a list, before asking the user the question again.

# The program must continuously ask the user for their order until the user enters "end".

# Upon ending the loop, the program will list out all of the user's orders. 

"""
Test Case 1
What would you like to order? Burger
What would you like to order? Coke
What would you like to order? Fries
What would you like to order? end


Output:
You have ordered the following:
1. Burger
2. Coke
3. Fries
"""


orderedfood=""
fooditems=[]
while True:
    orderedfood=input("What would you like to order?")
    if orderedfood =="end":
        break
    fooditems.append(orderedfood)

for i in range(len(fooditems)):
    print(str(i+1)+". "+fooditems[i])