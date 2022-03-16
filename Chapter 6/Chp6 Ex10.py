def mean_list(l: list):
    mean = 0
    for item in l:
        mean += item
    
    mean /= len(l)
    
    return mean

my_list = [1,2,3,4,5,6,7]

mean_of_list = mean_list(my_list)

print(mean_of_list)

input()
