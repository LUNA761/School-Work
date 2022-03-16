def sum_list(l: list):
    sum = 0
    for item in l:
        sum += item
    
    return sum

my_list = [1,2,3,4,5,6,7]

sum_of_list = sum_list(my_list)

print(sum_of_list)

input()
