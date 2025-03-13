allstud=""
numofstud=int(input("How many students are there in the class?"))
for i in range(numofstud):
    Student=input("Who is student #"+str(i+1)+" ?")
    allstud+=Student
    allstud+="   "
print(allstud)