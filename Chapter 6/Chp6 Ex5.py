def remove_five(l: list):
    for item in l:
        if item == 5:
            l.remove(5)

my_list = [5,6,7,2,6,7,43,7,5,3,7,8,9,43,2,6,8]

remove_five(my_list)

print(my_list)

input()
