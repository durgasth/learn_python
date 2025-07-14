#1.Grade Calculator
# Ask the user to enter marks (0–100) and print the grade:

# 90-100: A

# 80-89: B

# 70-79: C

# 60-69: D

# <60: Fail """
marks =int(input("Enter marks(0-100):"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")  
elif marks>=70 and marks<=79:
    print("Grade C") 
elif marks>=60 and marks<=69:
    print("Grade D") 
elif marks>=0 and marks<=60:
    print("fail") 
else:
    print("Please enter the marks between 0 to 100")       