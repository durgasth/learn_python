# Print the Multiplication Table of a Number
# Ask the user for a number and print its table (1 to 10).
# print(f"{num} x {i} = {num * i}")

number=int(input("Enter a number:"))
for i in range (1,10+1): #[1,2,3,4,5,6,7,8,9,10]
    print(f"{number} x {i} = {number * i}")