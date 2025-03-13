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

