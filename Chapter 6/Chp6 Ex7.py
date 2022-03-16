def unique_elements(l: list):
    iter = 0
    for item in l:
        l.remove(item)

        if item in l:
            return False

        iter += 1
    
    return True

unique_list = [1,2,3,4,5,6]
non_unique_list = [1,22,3,4,5,6,6,7,7, 44, 44]

print(unique_elements(unique_list))
print(unique_elements(non_unique_list))

input()
