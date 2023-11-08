def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get Input
num = int(input("Enter a number: "))

# Call the function
if prime(num):
    print("The number " + str(num) + " is a prime number.")
else:
    print("The number " + str(num) + " is not a prime number.")
