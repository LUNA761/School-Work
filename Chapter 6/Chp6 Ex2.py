def my_sort(data_list: list):
    new_list = []

    while data_list:
        minimum = data_list[0]
        for x in data_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)
    
    return new_list

list_to_sort = [-5, -23, 5, 0, 23, -6, 23, 67]

list_sorted = my_sort(list_to_sort)

print(list_sorted)

input()
