def number_to_words(n):

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return ones[n // 100] + " Hundred " + helper(n % 100)

    if n == 0:
        return "Zero"
    else:
        words = ""
        i = 0
        while n > 0:
            if n % 1000 != 0:
                words = helper(n % 1000) + " " + thousands[i] + " " + words
            n //= 1000
            i += 1
        return words.strip()

# Read integer from file
with open("new.txt", "r") as file:
    input_integer = int(file.readline().strip())

# Convert integer to words
integer_in_words = number_to_words(input_integer)

# Write result back to the file
with open("new.txt", "a") as file:
    file.write(integer_in_words)

print("Conversion completed and written to the file.")
