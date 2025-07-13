# 1. Print Numbers 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print the Multiplication Table of a Number
# Ask the user for a number and print its table (1 to 10).
# print(f"{num} x {i} = {num * i}")

# Take input from the user
num = int(input("Enter a number: "))

# Loop from 1 to 10 and print the multiplication
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Print All Even Numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

# 4. Calculate the Sum of Numbers from 1 to N
# Take input from the user
n = int(input("Enter a number: "))

# Calculate the sum using the formula
total = sum(range(1, n + 1))

# Display the result
print(f"The sum of numbers from 1 to {n} is: {total}")


# 5. Print Each Character of a String
# word = input("Enter a word: ")
# Durga
# D
# u
# r
# g
# a

# Take input from the user
word = input("Enter a word: ")

# Loop through each character and print it
for char in word:
    print(char)
