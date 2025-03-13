accountname=input("What is your bank account name?")
def menu(balance):
    print("--- Bank Account Menu ---\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Apply Interest\n5. Exit")
    option=input("Select an option (1-5):")
    if option == "1":
        deposit=int(input("How much do you want to deposit?"))
        balance += deposit
        menu(balance)
    elif option == "2":
        withdraw=int(input("How much do you want to withdraw?"))
        if withdraw < balance:
            balance -= withdraw
        else:
            print("Error. Cannot withdraw more than balance.")
        menu(balance)
    elif option == "3":
        print("Your current balance is $"+str(balance)+".")
        menu(balance)
    elif option == "4":
        number_of_months=int(input("How many months of interest do you want to put?"))
        balance=balance* 5/100 * number_of_months
        menu(balance)
    if option == "5":
        print("Thank you for using Sigma Bank. Bye bye.")
menu(0)
