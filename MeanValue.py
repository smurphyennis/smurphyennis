# Input 6 numbers (you can modify these values)
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))
num6 = float(input("Enter number 6: "))

# Calculate the mean
total = num1 + num2 + num3 + num4 + num5 + num6
count = 6  # Since you have 6 numbers
mean = total / count

# Print the mean
print("The mean of the 6 numbers is:", mean)
