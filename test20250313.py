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

temperature=int(input("What is your temperature?"))
cough=input("Do you have cough?")
running_nose=input("Do you have a running nose?")
sore_throat=input("Do you have a sore throat?")
if temperature > 37:
    print("Please go and see a doctor")
elif cough == "yes":
    