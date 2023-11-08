def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get Input
num = int(input("Enter a number: "))

# Call the function
result = check(num)

print("The number " + str(num) + " is " + result + ".")
