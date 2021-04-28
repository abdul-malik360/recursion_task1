# Defining a function called fibonacci
def fibonacci(x):
    # defining the fibonacci sequence
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x - 2) + fibonacci(x - 1)
# defining range from 1 to 20
for x in range(0, 20):

    # printing function that returns first 20 Fibonacci numbers
    print(fibonacci(x), end=" ")




