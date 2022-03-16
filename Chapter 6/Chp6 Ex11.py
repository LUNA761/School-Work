def list_of_deviation(l: list):
    mean = 0
    for item in l:
        mean += item
    
    mean /= len(l)

    deviations = {}
    
    for item in l:
        deviations[item] = item - mean
    
    return deviations

my_list = [1,2,3,4,5,6,7,8,9]

print(list_of_deviation(my_list))

input()