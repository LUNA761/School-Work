def print_even_upto(number: int):
    for i in range(number):
        i += 1

        if i % 2 == 0:
            print(i)

print_even_upto(int(input("Number ~ ")))

input()
