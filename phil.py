def prime(x):
    if x <= 1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

filtered = filter(prime, range(10))

print("Prime numbers are:", list(filtered))
