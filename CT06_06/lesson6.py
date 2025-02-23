# print("Hello from lesson 6")
# for i in range(10):
    # print(i)
# numberOfStudents=int(input("How many students are there?"))
# totalMarks=0
# average=0
# for i in range(numberOfStudents):
#     marks= int(input("How many marks did student number "+str(i+1)+" get?"))
#     totalMarks=totalMarks+marks
# print("The average score of all the students is "+str(totalMarks/numberOfStudents))
# **Task 1a**:
# for i in range(3):
#     print("Hello, World!")

# # **Task 1b**:
# for i in range(5):
#     print(i)

# # **Task 1c**:
# print("Hello, World!")

# # **Task 1d**:
# ifSKIBIDI = 5

# # **Task 1e**:
# print ("Hello, World!")
## Task 2: Name Errors
# Fix the errors in the following:

# **Task 2a**:
age="SKIBIDI"
print(age)

# **Task 2b**:
name = "Alice"
print(name)

# **Task 2c**:
x = 5
print(x)
# **Task 2d**:
print("Hello, World!")

# ---------------------------------------------------------------

## Task 3: Type Errors
# Fix the errors in the following:

# **Task 3a**:
age = 25
print(age + 1)

# **Task 3b**:
number = 10
print(number - 5)

# **Task 3c**:
print("Repeat" * 3)

# **Task 3d**:
year = 2023
print("The year is " + str(year))

# **Task 3e**:
x = 10
y = x / 2

# **Task 3f**:
end = 5
for i in range(end):
    print(i)










def greet_user(name):
    print("Hello, {name}!")

# Name Error 1: Undefined variable 'username' (should be 'user_name')
user_name = "Alice"
greet_user(user_name)

# Name Error 2: Undefined function 'display_message' (function not defined)
def display_message(Message):
    print("{Message}")
display_message("Welcome!")

# Name Error 3: Undefined variable 'age' (misspelled as 'ag')
age = 25
print(age)

# Name Error 4: Undefined variable 'result' (variable never assigned)
result="SKIBIDI"
print(result)

# Name Error 5: Undefined function 'calculate' (not defined anywhere)
def calculate(number,number2):
    print({number}+{number2})
output = calculate(5, 3)
print(output)









# A simple program with 5 compounded type errors to debug

def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def multiply_numbers(num1: int, num2: int) -> int:
    return num1 * num2

def greet_user(username: str) -> str:
    return "Hello, {username}!"

def display_result(result: int) -> None:
    print("The result is {result}")

def main():
    # Error 1: Passing a string instead of an integer
    sum_result = add_numbers("10", 20)
    
    # Error 2: Passing a list instead of an integer
    product_result = multiply_numbers([5], 10)
    
    # Error 3: Passing an integer instead of a string
    greeting = greet_user(12345)
    
    # Error 4: Passing a float instead of an integer
    display_result(15.5)
    
    # Error 5: Incorrect return type annotation
    def faulty_function() -> int:
        return "This should be an integer"
    
    result = faulty_function()
    print(result)

if __name__ == "__main__":
    main()




#     x = 10
#     y = 5
#     print(x+y)

# if True:
#     print("What's error here?")

# this_is_a_variable=0
# print(this_is_a_variable)

# for i in range(5):
#     print(i)