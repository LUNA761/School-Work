def factorial(number: int):
    fact = 1
    for num in range(2, number + 1):
        fact *= num
    return fact

print(factorial(int(input("Number ~ "))))

input()
