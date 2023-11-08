def f1(n):
    return lambda a: a*n
doub= f1(2)
trip= f1(3)
print(trip(11))