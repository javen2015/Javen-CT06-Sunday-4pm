# Question:

# The Singapore Mini-Car Club assigns a registration ID to each toy car. The format of the ID is as follows:

# It starts with exactly 2 capital letters, followed by 3 to 4 digits, and ends with 1 capital letter.

# Write a Python function that checks if a given registration ID is valid based on this format.

# Rules:

# The first two characters must be capital letters (A–Z).

# The next 3 or 4 characters must be digits (0–9).

# The final character must be a capital letter (A–Z).

# If the registration ID is valid, return "Valid"; otherwise, return "Invalid".

# Test Case 1
# Input: AB123C
# Output: Valid

# Test Case 2
# Input: XZ7890Z
# Output: Valid

# Test Case 3
# Input: A123BC
# Output: Invalid (only one starting letter)

# Test Case 4
# Input: QW12F
# Output: Invalid (only two digits)

# Expected Skills Tested:
# String indexing

# str.isalpha(), str.isdigit(), str.isupper()

# Length checking

# Logical conditions

# Would you like the code answer as well for this sample test?